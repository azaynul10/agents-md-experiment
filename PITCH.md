# Pitch: a methods post-mortem on measuring AGENTS.md

For the AAIF blog intake, by whichever route the current guidelines specify.
Submitted as a community contributor writing about personal experience with an
AAIF-hosted project.

## Proposed article

**Working title:** What I Got Wrong Trying to Measure AGENTS.md

**Format:** narrative, first person, roughly 1,350 words.

I built a small harness to test whether adding an AGENTS.md changes how a
coding agent behaves on an unfamiliar repository: a purpose-built Python CLI,
five tasks with pass conditions enforced by frozen check scripts, metrics
defined before logging, 30 runs across two arms.

The harness found nothing, and the interesting part is why. Pass rate was
15/15 in both arms. The turn-count gap was smaller than the variation within a
single arm. The one metric that did separate the arms was confounded by
construction: my executor was a script, and in one arm I had handed that
script the file listing the correct commands, so it skipped the discovery step
it was written to fail. A decoy file I planted to catch careless edits never
fired in 30 runs, which means that instrument was never validated.

The article is about the design errors, not about AGENTS.md. Four things I
would do differently: a real agent instead of a script, a fresh session per
run, one pre-registered endpoint, and a trap proven to fire before it counts
as an instrument.

**Why it may be useful:** the reversal in "Measuring AGENTS.md: What Five Runs
Show That One Doesn't" is the reason I report no separation instead of a win. A
worked example of a harness that failed, and of how to tell, seems worth having
next to the results that worked.

**Artifact:** code, data, all 30 transcripts, limitations and related work in a
public repository. The article text is unpublished and would be original to
AAIF.
