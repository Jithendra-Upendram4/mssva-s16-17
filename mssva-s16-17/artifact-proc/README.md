# Artifact Processor – Runtime & Supply‑Chain Security Lab

## Background

You are given a containerized **internal artifact processor** used inside an organization to process uploaded artifacts, extract metadata, and compute integrity information.

This service is **not internet‑facing** and is assumed to be deployed inside a trusted environment. It follows several good security practices by default, but like most real systems, it is **not perfectly secure**.

Your task is to analyze this artifact processor from a **security researcher’s perspective**.

This lab focuses on two important security dimensions:

- **Supply‑chain & dependency risk**
- **Runtime behavior & system interactions**

The goal is not to “run tools and copy output”, but to understand:
- what these tools are actually observing,
- what they *cannot* see,
- and what gaps still remain.

---

## What You Are Given

- A container image running an internal artifact processor
- Access to run security tools **outside** the container
- Ability to observe runtime behavior while the system is in use

You should treat this as a **real internal service**, not a CTF challenge.

---

## Objective

Identify **five security-relevant flags** present in the system.

Each flag represents a **design, configuration, dependency, or runtime behavior** that could matter in a real security review.

You are **not expected to exploit** anything.
You are expected to **observe, reason, and explain**.

---

## The Five Flags

You must identify **all five** of the following flags:

1. **Outdated or vulnerable dependency**
   - A dependency that introduces known risk
   - The system still functions correctly, but risk exists

2. **Unexpected file system modification**
   - A file write occurring outside the expected application workflow
   - Indicates behavior beyond pure artifact processing

3. **Hidden process execution**
   - Execution of a command or subprocess not directly visible at the application level
   - Occurs as part of normal operation, not an attack

4. **Suspicious process arguments**
   - A command is executed with arguments that would raise concern during a security review
   - Not necessarily malicious, but risky

5. **Trust boundary assumption**
   - An implicit assumption that input, environment, or execution context is trusted
   - Safe in some environments, dangerous in others

> You are **not told** which tool reveals which flag.  
> Some flags may require **correlating observations**.

---

## Your Task

- Analyze the artifact processor **as a running system**
- Observe:
  - dependencies
  - runtime behavior
  - system interactions
- Identify evidence for each of the five flags
- Document your findings clearly

---

## Deliverable

Create a short report (markdown or text) containing:
```text
| Flag | What you observed | Why it matters |
|-----:|------------------|----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
```
Focus on **reasoning**, not tool output screenshots.

---

## Important Notes

- Running a scanner does **not** mean security is complete
- Runtime tools observe behavior, not intent
- Supply‑chain tools find risk, not exploitability
- Real security work is about **context and judgment**

---

## What This Lab Is Teaching You

- Why scanners alone are insufficient
- Why runtime security exists even in “trusted” environments
- How internal services still create security signals
- How security teams reason beyond alerts

This is how security is practiced in real environments.
