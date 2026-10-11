# AI Interview Coach — Software Requirements Specification (SRS)

**Version:** 0.1  
**Status:** Draft — Pending Review  
**Related document:** Product Requirements Document (PRD) v0.1  
**Last updated:** October 11, 2026

## 1. Purpose

This document defines the functional and non-functional requirements for the AI Interview Coach system. It translates the product requirements into behaviors that can be implemented, tested, and verified.

The system enables users to practice interviews using platform-provided or user-created question sets, submit text or voice answers, receive AI-generated evaluations, and track their practice history and progress.

## 2. Scope

The initial system must support:

- User authentication and authorization.
- Browsing and managing question sets.
- Creating and editing custom question sets.
- Starting and managing interview practice sessions.
- Submitting text and voice answers.
- Evaluating saved answers using an AI service.
- Retrying failed evaluations without duplicating submissions.
- Preserving historical question versions.
- Tracking progress per question set and across a user's account.
- Handling validation failures, processing failures, and service outages.

## 3. Definitions

| Term | Definition |
|---|---|
| User | An authenticated person using the platform. |
| Question set | An ordered or unordered collection of interview questions. |
| Question version | The specific wording and relevant metadata of a question presented during practice. |
| Interview session | A practice session created from a particular question-set version. |
| Answer submission | A saved text or voice response associated with a question in a session. |
| Evaluation run | One attempt to evaluate a saved answer. |
| Completed evaluation | An evaluation run that has successfully produced and persisted a valid result. |
| Failed evaluation | An evaluation run that could not produce a valid result. |
| Set-level progress | Progress calculated from practice associated with a particular question set. |
| Account-level progress | Progress aggregated from eligible practice across the user's account. |

**Important distinction:** An answer submission represents what the user answered. An evaluation run represents an attempt to assess that answer. They are separate operations.

## 4. Actors and Permissions

### 4.1 User

An authenticated user can:
- Browse available platform question sets.
- Create and manage their own question sets.
- Start practice sessions.
- Submit and review their answers.
- Request evaluations and retry failed evaluations.
- View their practice history and progress.

A user must not access another user's private resources.

### 4.2 Platform administrator

Administrative management of platform-provided question sets is outside the initial detailed implementation scope. The required permissions and workflows must be defined before an administration interface is built.

### 4.3 External AI evaluation service

The AI service processes eligible saved answers and returns evaluation results. It is an external dependency and may be unavailable, return invalid output, or exceed configured processing limits.

The system must not assume that an external evaluation request always succeeds.

## 5. Functional Requirements

### 5.1 Authentication and authorization

**FR-AUTH-01 — Authentication**

The system must require authentication before a user accesses private practice history or manages private resources.

**FR-AUTH-02 — Resource ownership**

The system must verify that a user has permission to access or modify a requested question set, session, answer, or evaluation.

**FR-AUTH-03 — Unauthorized access**

The system must reject unauthorized requests without exposing private resource contents.

**FR-AUTH-04 — Ownership enforcement**

Ownership checks must be applied on the server, not only in the user interface.

### 5.2 Question-set management

**FR-SET-01 — Browse sets**

The system must allow users to retrieve available platform-provided question sets.

**FR-SET-02 — Create a set**

The system must allow a user to create a custom question set with a valid title and its supported metadata.

**FR-SET-03 — Add questions**

The system must validate and save questions added to a custom set.

**FR-SET-04 — Edit sets**

The system must allow an authorized user to edit their custom set according to the supported editing rules.

**FR-SET-05 — Remove questions**

The system must allow the owner to remove a question from the current version of a custom set.

**FR-SET-06 — Preserve historical meaning**

Editing or removing a question must not silently change the question that was presented in an earlier session.

**FR-SET-07 — Validate set content**

The system must reject a set or session configuration that does not satisfy the defined content requirements.

Exact title lengths, question limits, and other validation constraints must be established before implementation.

### 5.3 Interview sessions

**FR-SESSION-01 — Create session**

The system must create a practice session associated with a valid question set and the appropriate question-set version.

**FR-SESSION-02 — Present questions**

The system must provide the questions belonging to the session's selected question-set version.

**FR-SESSION-03 — Associate answers**

Every answer submission must be associated with the correct user, session, and question version.

**FR-SESSION-04 — Preserve history**

The system must retain sufficient historical information to identify the question and set version used in a previous session.

**FR-SESSION-05 — Session status**

The system must represent the session lifecycle using explicitly defined states. The final state model must be agreed upon before implementation.

### 5.4 Answer submission

**FR-ANSWER-01 — Text answer**

The system must accept a valid text answer and associate it with the selected question and session.

**FR-ANSWER-02 — Voice answer**

The system must accept a supported voice recording or audio submission and associate it with the selected question and session.

**FR-ANSWER-03 — Persist before evaluation**

The system must successfully persist an answer before attempting to evaluate it.

**FR-ANSWER-04 — Validation**

The system must reject answers that violate the agreed input constraints and provide a useful error message.

**FR-ANSWER-05 — Immutable submission history**

Once an answer has been submitted, retrying its evaluation must not overwrite or duplicate the original submission.

If editing or replacing an answer is later supported, the system must define whether that action creates a new submission or a new version.

**FR-ANSWER-06 — Voice transcription**

Where transcription is required, the system must associate the resulting transcript with the corresponding voice submission.

The system must handle transcription failure without incorrectly marking the answer as successfully evaluated.

**FR-ANSWER-07 — Submission acknowledgment**

The system must clearly distinguish an answer that has been saved from one that has only been entered into the interface.

### 5.5 Evaluation processing

**FR-EVAL-01 — Evaluate saved answers**

The system must evaluate an existing saved answer, rather than relying on unsaved client-side input.

**FR-EVAL-02 — Structured results**

A successful evaluation must return a valid, structured result conforming to the agreed evaluation contract.

**FR-EVAL-03 — Question-appropriate evaluation**

The evaluation process must use criteria appropriate to the question's category or type.

**FR-EVAL-04 — Persist successful evaluation**

A completed evaluation and its result must be persisted so the user can retrieve them later.

**FR-EVAL-05 — Record failures**

The system must record evaluation failures with a status and appropriate diagnostic information.

Internal diagnostics must not expose secrets or sensitive infrastructure details to the user.

**FR-EVAL-06 — Retry evaluation**

The system must allow a failed evaluation to be retried against the same saved answer, subject to the agreed retry policy.

**FR-EVAL-07 — Distinct evaluation runs**

Each retry must be represented as a distinct evaluation run. The original failed run must remain part of the history.

**FR-EVAL-08 — No duplicate answer**

Retrying an evaluation must not create a new answer submission.

**FR-EVAL-09 — Prevent conflicting concurrent work**

The system must define how simultaneous evaluation requests for the same answer are handled so that duplicate work does not unintentionally corrupt state or metrics.

**FR-EVAL-10 — External service failures**

Timeouts, rate limits, network failures, and invalid AI output must be handled without losing the saved answer.

**FR-EVAL-11 — Valid result requirement**

An evaluation must not be marked completed until the returned result passes the required validation and is successfully persisted.

**FR-EVAL-12 — User-visible status**

The interface must communicate whether an evaluation is pending, processing, completed, or failed.

### 5.6 Evaluation lifecycle

The following is the proposed evaluation state model:

| State | Meaning |
|---|---|
| `pending` | An evaluation has been requested but processing has not started. |
| `in_progress` | The system is processing the evaluation. |
| `completed` | A valid evaluation result has been persisted. |
| `failed` | The evaluation attempt failed and did not produce a valid persisted result. |

The allowed transitions are:

- `pending` → `in_progress`
- `in_progress` → `completed`
- `in_progress` → `failed`
- `failed` → a new evaluation run in `pending`

A retry creates a **new evaluation run**. It does not reset the original failed run or create a new answer.

The final implementation must also define how abandoned or interrupted processing is recovered, including cases where a worker stops unexpectedly.

### 5.7 Progress tracking

**FR-PROGRESS-01 — Set-level progress**

The system must calculate progress using eligible practice activity associated with a question set.

**FR-PROGRESS-02 — Account-level progress**

The system must calculate account-level progress using eligible activity across the user's question sets.

**FR-PROGRESS-03 — Completed evaluations only**

Failed and pending evaluations must not contribute to completed-evaluation metrics.

**FR-PROGRESS-04 — Retry accounting**

Retrying an evaluation must not increase the answer-submission count.

**FR-PROGRESS-05 — Historical results**

Historical evaluation results must remain available after a question set is edited.

**FR-PROGRESS-06 — Consistent aggregation**

The same defined eligibility rules must be applied consistently to set-level and account-level calculations.

**FR-PROGRESS-07 — Transparent metrics**

The system must distinguish counts of submitted answers, completed evaluations, failed evaluations, and practice sessions where those metrics are displayed.

The following calculations are proposed starting points, pending approval:

- **Answer submission count:** number of distinct saved answer submissions.
- **Completed evaluation count:** number of successfully persisted evaluations.
- **Evaluation success rate:** successful evaluation runs divided by all eligible evaluation runs, excluding runs that have not yet reached a terminal state.
- **Practice completion rate:** completed sessions divided by sessions eligible for the chosen calculation.

A single universal performance score should not be implemented until the aggregation rules and treatment of repeated practice are agreed upon.

### 5.8 History and retrieval

**FR-HISTORY-01**

Users must be able to retrieve their previous sessions.

**FR-HISTORY-02**

Users must be able to retrieve saved answers associated with their sessions.

**FR-HISTORY-03**

Users must be able to retrieve completed evaluation results associated with their answers.

**FR-HISTORY-04**

The system must preserve the relationship between a historical answer, the question version presented, and its evaluation runs.

**FR-HISTORY-05**

History retrieval must enforce user authorization.

## 6. Input Validation Requirements

The system must validate inputs at the appropriate server-side boundaries.

| Input | Required behavior |
|---|---|
| Question-set title | Reject missing or invalid titles. |
| Question text | Reject missing or invalid question content. |
| Text answer | Reject empty or otherwise invalid submissions according to the agreed policy. |
| Voice answer | Validate supported format, size, and other configured constraints. |
| Resource identifier | Reject malformed identifiers and verify resource existence and ownership. |
| Evaluation request | Verify that the target answer exists and is eligible for evaluation or retry. |
| AI result | Validate required fields, types, and permitted values before persistence. |

Exact length limits, file constraints, and evaluation schema details must be documented before implementation.

Validation errors must be distinguishable from authorization failures, missing resources, and unexpected processing failures.

## 7. Error Handling Requirements

The system must handle at least the following conditions:

| Condition | Expected behavior |
|---|---|
| Invalid input | Reject the request and explain which input is invalid. |
| Unauthenticated request | Require authentication. |
| Unauthorized resource access | Reject access without disclosing private contents. |
| Resource not found | Return an appropriate not-found response. |
| Duplicate concurrent evaluation request | Apply the agreed concurrency policy without creating duplicate answer submissions. |
| AI service timeout | Record or recover the failed run according to the retry policy; preserve the answer. |
| AI service rate limit | Handle the failure without losing the answer and communicate the status. |
| Invalid AI response | Reject the invalid result and do not mark the run completed. |
| Persistence failure | Do not report success unless the required data was successfully persisted. |
| Audio transcription failure | Preserve available submission information and report the failure clearly. |
| Unexpected server error | Return a safe error response and retain diagnostic information where possible. |

The HTTP status codes and API error response schema will be defined in the API specification.

## 8. Non-Functional Requirements

### NFR-01 — Security

Private resources must be protected by server-side authorization. Sensitive credentials and API keys must not be exposed to the client.

### NFR-02 — Data integrity

Saved answers, evaluation runs, and historical question versions must remain correctly associated.

### NFR-03 — Reliability

Temporary failures in AI evaluation must not cause the system to lose previously saved answers.

### NFR-04 — Observability

The system must provide enough operational logging to investigate failed evaluation runs without unnecessarily logging private answer content or credentials.

### NFR-05 — Performance

The system should respond promptly to ordinary operations. Evaluation and transcription operations must expose processing status when they take longer.

Specific latency targets and expected load must be agreed upon before launch.

### NFR-06 — Privacy

Audio, transcripts, and answers must be handled according to documented retention, deletion, and processing policies.

### NFR-07 — Maintainability

The evaluation contract, state transitions, validation rules, and progress calculations must be documented and testable.

### NFR-08 — Accessibility

Core practice flows must provide understandable feedback and support both text and voice input modes.

## 9. Acceptance Criteria

The following are initial, testable scenarios.

### Scenario A: Save and evaluate a text answer

**Given** an authenticated user is practicing a valid question set,

**When** the user submits a valid text answer and requests evaluation,

**Then** the system saves the answer, associates it with the correct session and question, evaluates the saved submission, and makes the completed result retrievable.

### Scenario B: Recover from evaluation failure

**Given** an answer has been saved and its evaluation has failed,

**When** the user retries the evaluation,

**Then** the system creates a new evaluation run for the same answer, preserves the original failed run, and does not create a duplicate answer submission.

### Scenario C: Invalid AI result

**Given** an evaluation is in progress,

**When** the AI service returns output that fails the evaluation schema validation,

**Then** the system must not mark the evaluation completed or expose the invalid result as a valid evaluation.

### Scenario D: Question-set edit

**Given** a user has completed a practice session,

**When** the user edits a question in their question set,

**Then** the previous session must continue to identify the original question version presented.

### Scenario E: Progress accounting

**Given** a user has submitted an answer with one failed evaluation run and one completed retry,

**When** the system calculates progress,

**Then** the answer counts as one distinct submission, the successful run counts as a completed evaluation, and the failed run remains visible in evaluation history.

### Scenario F: Authorization

**Given** a user attempts to retrieve another user's private answer,

**When** the system processes the request,

**Then** it denies access and does not disclose the answer's private content.

### Scenario G: Voice submission

**Given** an authenticated user submits a supported voice answer,

**When** the submission is accepted,

**Then** the system preserves its association with the relevant question and session and handles transcription or evaluation failures without incorrectly marking the evaluation completed.

### Scenario H: Persistence failure

**Given** an evaluation result has been generated,

**When** the system cannot persist the result,

**Then** it must not report the evaluation as successfully completed.

## 10. Dependencies

The system depends on:
- An authentication mechanism.
- Persistent storage for user resources and practice history.
- An AI evaluation service.
- A voice transcription capability, if required by the chosen voice workflow.
- An audio storage mechanism, if audio retention is approved.
- A deployment and monitoring environment.

Specific vendors and implementation choices are deliberately excluded from this requirements document.

## 11. Outstanding Decisions

The following items require resolution before implementation:

1. Exact validation limits for question sets, questions, and answers.
2. The final evaluation-result schema and rubric by question type.
3. The retry policy, including automatic retries, user-triggered retries, and retry limits.
4. Concurrent evaluation request behavior.
5. Recovery behavior for evaluations interrupted while in progress.
6. Rules for editing, replacing, or deleting submitted answers.
7. Session states and rules for skipping or completing questions.
8. Final progress aggregation rules, especially for repeated practice.
9. Audio retention, transcript retention, consent, and deletion requirements.
10. API response schemas and HTTP status codes.
11. Performance targets and expected usage.
12. Administrative permissions for platform-provided question sets.

## 12. Completion Criteria

This SRS can be approved when:

- Functional requirements are testable.
- The answer-submission and evaluation-run distinction is explicit.
- Evaluation lifecycle and retry semantics are agreed upon.
- Validation and failure behavior are sufficiently specified.
- Historical question versions and progress accounting are defined.
- Security and privacy requirements are accepted.
- Open decisions are resolved or explicitly deferred with agreed owners.

**Status:** Draft awaiting review. No database schema, endpoint implementation, or infrastructure design is approved solely by this document.