---
type: Playbook
title: ChatGPT Project Context and File Surfaces
description: Distinguish ChatGPT Project instructions, Project files, Library files, chat attachments, runtime copies, and Skills without inventing shared identity or lifecycle semantics.
status: reviewed
scope: ChatGPT Projects, files, Library, and Skills
confidence: medium
timestamp: 2026-09-16T02:02:00+08:00
last_verified: 2026-09-16
review_after: 2026-12-16
tags: [chatgpt, projects, files, library, skills, context]
---

# ChatGPT Project Context and File Surfaces

ChatGPT Projects can keep chats, files, instructions, and related context together.
Treat those product surfaces as distinct unless official documentation explicitly
states that they share identity or lifecycle semantics.

## Documented Product Model

- **Project instructions** apply inside that Project and override global custom
  instructions for chats in the Project.
- **Project files** are reference material attached to the Project. They can be
  previewed, downloaded, or deleted from the Project sources list.
- Uploading a Project file with the same name as an existing one can produce an
  explicit choice to upload it anyway or skip it; same display name therefore
  does not imply replacement.
- **Library** stores uploaded and created ChatGPT files for later reuse when the
  feature is available. Library files and chats are managed separately.
- Files uploaded to a Project are retained with the Project until the Project is
  deleted, subject to OpenAI retention and legal/security exceptions.
- **Skills** are reusable workflows for repeatable tasks. Projects provide shared
  context, files, instructions, and conversations around an ongoing body of work.

## Safe Operating Rules

1. Keep one clearly named canonical instruction source when a Project also uses
   instruction files as reference material. Remove stale duplicates through the
   product surface that owns them.
2. Do not infer overwrite, replacement, or object identity from display-name
   equality alone.
3. When freshness matters, explicitly request the current instruction/source file
   rather than assuming every Project file has already been read in the current
   chat.
4. Keep volatile repository state in repository truth, not in reusable Project
   instructions:

   ```text
   Project instructions
     -> shared Project-wide behavior

   repo/AGENTS.md
     -> durable repository rules

   repo/CONTEXT.md
     -> current-only restart state

   Issue / PR / Git
     -> active task, evidence, and durable history
   ```

5. Prefer **Project instructions** for behavior that should apply throughout one
   Project. Prefer a **Skill** when the behavior is a reusable workflow that
   benefits from explicit packaging and reuse across chats or surfaces.
6. Keep repository-specific authority in the repository even when Project
   instructions or Skills provide higher-level workflow guidance.

## Empirical Observations, Not Product Guarantees

The following observations motivated this playbook but are not established by the
cited product documentation and should remain dated observations until OpenAI
publishes stronger guarantees:

- a tool-visible or runtime-mounted copy may be separate from the Project Source
  object shown in the UI;
- renaming or deleting a runtime copy may not mutate the Project Source card;
- internal file identity may differ from the display filename;
- recreating a runtime file with the same filename does not prove that a Project
  Source or Library object was replaced;
- source retrieval may be selective rather than equivalent to injecting every
  complete Project file into every prompt.

Operational consequence: **do not use a runtime filename or local working copy as
lifecycle authority for a Project Source or Library object.** Manage the product
object through the product surface that owns it unless a documented tool/API says
otherwise.

## Validation Checklist

Before relying on a Project/file behavior:

- identify the exact surface: Project instructions, Project file, Library file,
  chat attachment, Skill resource, or runtime/tool-visible copy;
- check current OpenAI documentation for retention and deletion semantics;
- verify same-name behavior instead of assuming overwrite;
- distinguish documented behavior from local observation;
- keep product-specific claims dated because ChatGPT behavior can change.

## Citations

- https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt
- https://help.openai.com/en/articles/20001052
- https://help.openai.com/en/articles/8983778
- https://help.openai.com/en/articles/8983762
- https://help.openai.com/en/articles/20001066
- https://openai.com/academy/skills/
