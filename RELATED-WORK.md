# Related work

Four public evaluations of AGENTS.md-style context files that I found while
writing up this repository. I did not do a systematic literature review, so
this is not a survey and there are likely others.

For each, I state where this repository stands relative to it. The short
version: all four are stronger designs than mine. My limitations are in
`harness/LIMITATIONS.md`.

## 1. Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

Gloaguen et al., SRI Lab, ETH Zurich.
https://arxiv.org/html/2602.11988 ,
https://www.sri.inf.ethz.ch/publications/gloaguen2026agentsmd

Introduces AGENTBENCH: 138 instances across 12 repositories that carry
developer-written context files, plus SWE-bench Lite for LLM-generated ones.
Multiple coding agents and multiple LLMs. Reports that context files produce
no improvement in task success rate, while **increasing inference cost by over
20%**, and that context files drive broader exploration and more testing.

**My position.** My null on pass rate is consistent with theirs, but mine
carries far less weight: they used real agents on real repository issues, I
used a scripted policy on one synthetic CLI. On their cost finding **my design
cannot speak to cost at all** — a scripted policy consumes no tokens and I
measured neither tokens nor wall-clock time (`harness/LIMITATIONS.md` L8). If
their 20% cost figure holds, it is the most decision-relevant number of the
four, and my harness is blind to it.

## 2. On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents

https://arxiv.org/abs/2601.20404v1 ,
https://assets.empirical-software.engineering/pdf/jaws26-agents.md-efficiency.pdf

10 repositories, 124 pull requests, paired runs with and without AGENTS.md,
holding task and repository snapshot constant. Reports lower median runtime
(28.64%) and reduced output token consumption (16.58%), with comparable task
completion.

**My position.** This is the closest design to what I was attempting: same
task, same repo, presence or absence of the file. They measured runtime and
tokens on real agents across 124 real pull requests. I measured turn counts
from a script across 5 synthetic tasks. Their efficiency result and my
turn-count difference are not comparable, and mine should not be read as
support for theirs: my gap of 1.7 turns is smaller than my own within-arm
spread of 2, and it is mechanical (`harness/LIMITATIONS.md` L4).

## 3. Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories

https://arxiv.org/html/2607.27250

288 evaluated runs, two frontier agents from different providers (Claude Code
and Codex), 17 real tasks from 3 repositories, three context-injection
strategies, hidden gold-test evaluation, equivalence testing (TOST) to bound
the null rather than merely fail to reject it. Finds no measurable movement in
correctness, bounded to roughly 10 to 15 percentage points, and attributes
failures to implementation skill rather than missing repository knowledge. It
also finds that borderline task difficulty is agent-specific, which it offers
as an explanation for why earlier single-agent studies disagree.

**My position.** This is the design my v2 list is pointing at, and it already
exists: multiple agent families, repeats, pre-specified analysis, bounded null.
Two things it does that mine does not. It **bounds** its null; I only report
that my checks failed to discriminate, which is a weaker statement. And its
manipulation probe confirms the context file never converts a near-miss into a
pass — that is a validated instrument, whereas my decoy-file trap never fired
in 30 runs and is therefore unvalidated (`harness/LIMITATIONS.md` L5). Their
finding that results do not transfer across agent families is also the direct
argument against drawing anything from my single-executor design.

## 4. Measuring AGENTS.md: What Five Runs Show That One Doesn't

Andrea Griffiths, on the Agentic AI Foundation blog.
https://aaif.io/blog/measuring-agents-md-what-five-runs-show-that-one-doesn-t

One real repository (a VS Code extension), GitHub Copilot CLI in
non-interactive mode, two tasks (one ambiguous, one multi-file), five runs per
condition, medians rather than single samples. Reports AGENTS.md ahead on both
tasks: 27% lower wall time, 24% fewer credits and 26% smaller diffs on the
ambiguous task, and a 9 to 10% median win on the multi-file task. The
methodological core of the post is a reversal: the first attempt, at one run
per condition, showed AGENTS.md 44% slower and 41% more expensive, and that
conclusion was wrong.

**My position.** This is the one that most directly indicts my design.

- **My 3 runs per cell with a scripted executor is strictly less informative
  than her 5 runs per cell with a real agent.** She varied the thing that
  actually matters (a live agent) and repeated enough to see that per-run noise
  had pointed her the wrong way. I repeated three fixed exploration variants of
  a script, which produces tidy spreads that understate real variance
  (`harness/LIMITATIONS.md` L7).
- Her n=1 to n=5 reversal is the reason I report no separation on a 1.7-turn
  gap instead of claiming an improvement. On a design weaker than hers, a gap
  that small is not something I can stand behind.
- Her result is positive and my result is null. **These do not conflict,
  because mine is not a measurement of agent behaviour at all** — it is a
  measurement of a script (`harness/LIMITATIONS.md` L1). My null is not
  evidence against her finding.
