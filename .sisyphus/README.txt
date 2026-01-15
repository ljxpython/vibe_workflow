This directory is reserved for oh-my-opencode orchestration.

- Prometheus (planner) writes plans to: .sisyphus/plans/
- Prometheus may use drafts in: .sisyphus/drafts/
- /start-work reads from .sisyphus/plans/ and executes the plan.

Vibe methodology docs live in ./plans/ (separate from orchestration runtime state).
