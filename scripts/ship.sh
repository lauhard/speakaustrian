#!/usr/bin/env bash
# Ship the current branch (D23): push, open a PR, wait for CI + preview build, squash-merge,
# wait for the production deploy. Usage: scripts/ship.sh "PR title" "PR body"
set -euo pipefail
branch=$(git rev-parse --abbrev-ref HEAD)
[ "$branch" != "main" ] || { echo "refusing to ship from main"; exit 1; }
git push -q -u origin "$branch"
foot=$'\n\n🤖 Generated with [Claude Code](https://claude.com/claude-code)'
pr=$(gh api "repos/{owner}/{repo}/pulls" -f base=main -f head="$branch" -f title="$1" -f body="$2$foot${CLAUDE_SESSION_URL:+$'\n\n'$CLAUDE_SESSION_URL}" --jq '.number')
wait_checks() { # $1 = ref, $2 = minimum number of checks
	local runs
	until runs=$(gh api "repos/{owner}/{repo}/commits/$1/check-runs" --jq '[.check_runs[] | .status] | "\(length) \(map(select(. != "completed")) | length)"') &&
		[ "${runs%% *}" -ge "$2" ] && [ "${runs##* }" = "0" ]; do sleep 10; done
	gh api "repos/{owner}/{repo}/commits/$1/check-runs" --jq '.check_runs[] | "\(.name): \(.conclusion)"'
}
out=$(wait_checks "$branch" 2); echo "$out"
echo "$out" | grep -qv "success" && { echo "PR #$pr: checks failed, not merged"; exit 1; }
sha=$(gh api -X PUT "repos/{owner}/{repo}/pulls/$pr/merge" -f merge_method=squash --jq '.sha')
out=$(wait_checks "$sha" 2); echo "$out"
echo "$out" | grep -qv "success" && { echo "PR #$pr merged, but the production build failed"; exit 1; }
git switch -q main && git pull -q --ff-only
echo "PR #$pr merged and deployed"
