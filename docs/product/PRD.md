# AI Interview Coach — Product Requirements Document (PRD)

**Version:** 0.1  
**Status:** Draft — Pending Review  
**Document owner:** Product & Engineering  
**Last updated:** October 11, 2026

---

## 1. Product Overview

### 1.1 Product vision

Build an AI-powered interview preparation platform that enables job seekers to practice realistic interviews, receive actionable feedback on their answers, and track their improvement over time.

Users can practice using existing question sets, including company-specific and role-specific questions, or create and manage their own interview sets. They can answer questions using text or voice and receive AI-generated evaluations.

### 1.2 Problem statement

Job seekers often struggle to prepare effectively for interviews because:

- They lack access to realistic interview practice.
- They may not know whether their answers are clear, relevant, or sufficiently detailed.
- They receive limited personalized feedback when practicing alone.
- They have difficulty identifying recurring weaknesses.
- They lack a structured way to measure progress across multiple practice sessions.

The product addresses these problems by combining interview practice, AI-powered feedback, and persistent progress tracking in one platform.

### 1.3 Proposed solution

The platform will allow users to:

1. Browse available interview question sets.
2. Create their own sets of questions.
3. Start an interview practice session.
4. Submit answers through text or voice.
5. Request an AI evaluation for each saved answer.
6. Review feedback and suggested improvements.
7. Retry an evaluation if the evaluation process fails.
8. Review performance within a specific question set.
9. Track overall progress across their account.

---

## 2. Goals and Non-Goals

### 2.1 Product goals

- Provide a practical environment for interview preparation.
- Support both typed and spoken answers from the initial release.
- Deliver useful, consistent, and explainable feedback.
- Preserve previous answers and evaluations.
- Allow users to track progress per question set and across their account.
- Support both platform-provided and user-created question sets.
- Handle technical evaluation failures without losing submitted answers.
- Establish a foundation for future interview preparation features.

### 2.2 Non-goals for the initial release

The initial release will not aim to provide:

- Live interviews with human interviewers.
- Automated job applications or recruiter communication.
- Guaranteed predictions of hiring outcomes.
- Facial-expression, emotion, or personality inference.
- A social network or public leaderboard.
- Real-time conversational interviewing with an AI avatar.
- Full speech coaching, such as detailed accent or pronunciation analysis, unless explicitly included in a later scope decision.

These are excluded from the initial scope to keep the product focused on practice, answer evaluation, and progress tracking.

---

## 3. Target Users

### 3.1 Primary persona: Job seeker

A person preparing for interviews who wants to practice answering questions, understand weaknesses, and improve before an actual interview.

**Needs:**
- Relevant interview questions.
- Convenient text and voice practice.
- Actionable feedback.
- A record of previous attempts.
- Evidence of improvement over time.

### 3.2 Secondary persona: Self-directed learner

A person preparing for a particular role, company, or competency who wants to organize custom questions and practice repeatedly.

**Needs:**
- Create and edit personal question sets.
- Organize questions by topic or purpose.
- Revisit previous answers.
- Compare performance over time.

### 3.3 Future persona: Platform administrator

An authorized person responsible for managing platform-provided question sets and maintaining their quality.

Administrative capabilities will require further definition before implementation.

---

## 4. Product Scope

### 4.1 User accounts and history

Users should have an account associated with their practice history.

The platform should allow authenticated users to:
- Access their question sets and interview history.
- Review previously submitted answers.
- Review completed evaluations.
- View their progress summaries.

Account registration methods, password recovery, and authentication options will be specified in the requirements document.

### 4.2 Platform-provided question sets

The platform will offer ready-made interview question sets.

Examples may include:
- Fresh graduate interviews.
- Behavioral interviews.
- Technical interviews.
- Role-specific interviews.
- Company-specific interview preparation.

Each set should have enough descriptive information for users to understand its intended audience and purpose.

The availability of company-specific questions must not imply that the platform has access to confidential or official interview questions unless their provenance can be established.

### 4.3 User-created question sets

Users should be able to create and manage their own question sets.

At minimum, the product should support:
- Creating a set with a title and description.
- Adding questions.
- Editing question text.
- Removing questions.
- Viewing the questions in a set.
- Practicing using the set.

The product must define what happens when a user edits a set that already has practice history. Previous sessions must remain interpretable against the questions that were presented at the time.

### 4.4 Interview practice

Users should be able to start a practice session using a selected question set.

A session should provide a structured way to:
- Present questions.
- Capture and save answers.
- Associate each answer with the correct question and session.
- Request an evaluation.
- Review the evaluation result.

Whether users can skip questions, pause sessions, or answer questions in a custom order remains to be finalized.

### 4.5 Answer submission

The product will support two answer modes from the initial release.

**Text mode**
- The user types an answer.
- The platform validates and saves the submitted text.
- The saved answer can be evaluated.

**Voice mode**
- The user records or otherwise provides a spoken answer.
- The platform processes the audio and obtains text for evaluation, where transcription is required.
- The product preserves the relationship between the original submission, any transcript, and the evaluation.

The exact audio recording, transcription, file retention, and consent requirements will be defined in the technical and privacy requirements.

A saved answer must not be silently replaced when the user requests an evaluation retry.

### 4.6 AI answer evaluation

The system will evaluate submitted answers and provide feedback intended to help the user improve.

Potential evaluation dimensions include:
- Relevance to the question.
- Clarity and structure.
- Completeness of the answer.
- Specificity and supporting examples.
- Communication effectiveness.
- Technical correctness, when applicable to the question.

The final criteria will depend on question type. For example, a behavioral question and a technical question should not necessarily use the same rubric.

The evaluation should provide more than a score: it should help the user understand what worked, what was missing, and how the answer could be improved.

AI-generated feedback must be presented as guidance rather than a guaranteed prediction of interview or hiring success.

### 4.7 Evaluation failure and retry

An answer submission and its evaluation are separate product records.

If an answer has been saved but its evaluation fails:
- The submitted answer remains available.
- The failed evaluation is recorded with an appropriate status.
- The user can request another evaluation of that same saved answer.
- Retrying evaluation must not create a duplicate answer submission.
- A failed evaluation must not count as a completed evaluation in performance summaries.

The product must distinguish an evaluation that is pending, in progress, completed, or failed. The exact status transitions and retry limits will be specified in the Software Requirements Specification.

### 4.8 Progress tracking

The platform will provide progress at two levels.

**Question-set progress**

Users can review performance associated with a particular question set, including completed practice and evaluation history.

**Overall account progress**

Users can review an account-wide summary that aggregates eligible practice activity across their question sets.

Progress calculations must use defined, consistent rules. Failed evaluations must not be treated as successful completed evaluations, and repeated evaluations of the same answer must not accidentally inflate the number of answers submitted.

Historical results should remain available even when a question set is edited.

---

## 5. Core User Journeys

### Journey A: Practice using a platform question set

1. The user signs in.
2. The user browses available question sets.
3. The user selects a set relevant to their target role or interview.
4. The user starts a practice session.
5. The system presents a question.
6. The user submits a text or voice answer.
7. The system saves the answer.
8. The user requests an evaluation.
9. The system evaluates the saved answer.
10. The user reviews the feedback.
11. The user continues practicing.
12. The system updates eligible set-level and account-level progress.

### Journey B: Create a custom question set

1. The user opens question-set management.
2. The user creates a new set.
3. The user enters a title and optional description.
4. The user adds questions.
5. The user saves the set.
6. The user starts a practice session using the set.
7. The user submits answers and requests evaluations.
8. The system records the resulting practice history and progress.

### Journey C: Retry a failed evaluation

1. The user submits an answer.
2. The system saves the answer.
3. The evaluation process fails.
4. The system records the failure and informs the user.
5. The user selects the retry-evaluation action.
6. The system evaluates the existing saved answer again.
7. The system records the new evaluation run.
8. If successful, the result becomes available for review and eligible progress calculations.

The user should not have to retype or rerecord an answer merely because the evaluation service failed.

### Journey D: Review progress

1. The user opens their progress dashboard.
2. The user reviews account-wide progress.
3. The user selects a question set.
4. The system displays the practice and evaluation history for that set.
5. The user reviews previous feedback to identify areas for improvement.

---

## 6. Product-Level Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| PR-01 | Users can access their own practice history. | Must |
| PR-02 | Users can browse platform-provided question sets. | Must |
| PR-03 | Users can create and manage custom question sets. | Must |
| PR-04 | Users can start practice sessions from a question set. | Must |
| PR-05 | Users can submit text answers. | Must |
| PR-06 | Users can submit voice answers. | Must |
| PR-07 | The system saves answers before evaluation begins. | Must |
| PR-08 | The system can evaluate a saved answer and return structured feedback. | Must |
| PR-09 | Users can retry a failed evaluation without submitting a duplicate answer. | Must |
| PR-10 | The system preserves the history of evaluation attempts. | Must |
| PR-11 | Users can review previous answers and completed evaluations. | Must |
| PR-12 | Users can review progress for an individual question set. | Must |
| PR-13 | Users can review overall account progress. | Must |
| PR-14 | Historical practice remains associated with the question version originally presented. | Must |
| PR-15 | Failed evaluations are excluded from completed-evaluation metrics. | Must |
| PR-16 | The platform provides useful question-set metadata. | Should |
| PR-17 | The system can distinguish evaluation lifecycle states. | Must |

These are product-level requirements. Detailed validation rules, API behavior, data constraints, authorization, error handling, and status transitions belong in the SRS.

---

## 7. Non-Functional Product Expectations

### Reliability
Saved answers and completed evaluations should remain available when users revisit their history. Temporary evaluation failures should not destroy previously saved submissions.

### Performance
The interface should respond promptly to ordinary user actions. AI evaluation and voice processing may take longer than standard requests; the product should communicate their status rather than appearing frozen.

Specific response-time targets will be established after technical constraints and expected usage are assessed.

### Security and privacy
Users must not be able to access another user's private answers, custom question sets, or practice history without authorization.

The product must establish policies for audio, transcripts, user-generated content, and AI processing before launch.

### Usability and accessibility
The main practice flow should be understandable without specialized technical knowledge. Text and voice practice should have clear status indicators and understandable error messages.

### Maintainability
Product behavior and evaluation rules should be documented so that future changes can be implemented and tested consistently.

---

## 8. Success Metrics

The product should be evaluated using measurable indicators rather than relying only on the presence of features.

Proposed metrics include:

- **Practice activation:** percentage of new users who complete their first answer submission.
- **Evaluation completion rate:** percentage of evaluation requests that complete successfully.
- **Evaluation recovery rate:** percentage of failed evaluations that later succeed after retry.
- **Practice retention:** percentage of users who return to practice after their first session.
- **Practice completion:** percentage of started sessions that reach the defined completion condition.
- **Feedback usefulness:** user ratings or feedback on the usefulness of evaluations.
- **Progress engagement:** percentage of users who revisit their progress dashboard.

The exact metric definitions, measurement windows, and target values will be finalized before launch. Failed evaluations and evaluation retries must be counted consistently to avoid misleading results.

---

## 9. Constraints and Assumptions

### Constraints
- AI evaluations may fail because of service outages, rate limits, invalid responses, or network problems.
- Voice processing may introduce transcription errors.
- AI-generated evaluations may be inconsistent or incorrect.
- Company-specific question content must be handled responsibly.
- The product must preserve historical results when question sets change.

### Assumptions
- Users want both immediate feedback and a record of previous performance.
- Users may practice the same question multiple times.
- A single user may maintain multiple question sets.
- Users may prefer different answer modes for different questions.
- Evaluation retries should not be counted as new answer submissions.

These assumptions should be validated as the product design develops.

---

## 10. Risks and Mitigations

| Risk | Proposed mitigation |
|---|---|
| AI feedback is inaccurate or generic. | Use question-appropriate evaluation criteria, structured feedback, and quality tests. |
| Voice transcription changes the meaning of an answer. | Preserve transcript provenance and communicate transcription limitations. |
| Evaluation failures cause lost work. | Save submissions independently from evaluation and support retries. |
| Editing a question changes the meaning of old results. | Preserve the question version associated with each historical session. |
| Progress metrics become misleading. | Define aggregation rules and exclude failed or duplicate activity appropriately. |
| User answers or audio are exposed. | Apply authorization, data minimization, and explicit retention policies. |
| Users interpret scores as hiring predictions. | Explain the scope and limitations of AI-generated feedback. |

---

## 11. Open Product Decisions

These decisions should be resolved during PRD review or in the next requirements documents.

1. **Evaluation rubric:** Which criteria apply to behavioral, technical, and general interview questions?
2. **Scoring:** Should the product use numerical scores, descriptive ratings, written feedback, or a combination?
3. **Progress aggregation:** How should overall progress combine results from different question sets and evaluation rubrics?
4. **Repeated practice:** Should users see their latest result, best result, historical trend, or all three?
5. **Session behavior:** Can users skip questions, pause sessions, or revisit questions before submitting?
6. **Voice processing:** Is audio stored, or is only the transcript retained? What consent and deletion controls are required?
7. **Custom-set visibility:** Are custom sets private by default? Can users share or publish them?
8. **Question-set ownership:** What happens to practice history if a user deletes a set?
9. **Platform content management:** How are official question sets reviewed and updated?
10. **Authentication:** Which registration and sign-in methods are required for the first release?
11. **AI service limits:** What retry limits and user-facing behavior are appropriate when an evaluation repeatedly fails?
12. **Launch scope:** Which question categories and supported languages must be available at launch?

---

## 12. Acceptance Criteria for PRD Approval

The PRD is ready for approval when:

- The target users and primary problem are clearly defined.
- The MVP scope and non-goals are agreed upon.
- Text and voice answer submission are included.
- The distinction between answer submission and evaluation is explicit.
- Evaluation retry behavior is documented.
- Question-set history and versioning expectations are documented.
- Set-level and account-level progress are defined as product capabilities.
- Success metrics are agreed upon or explicitly deferred.
- Open decisions have owners or a planned resolution stage.

**Current status:** Draft awaiting review. No architecture or database implementation decisions are approved by this document alone.

**Next step:** Review and approve this PRD. After approval, create the Software Requirements Specification (SRS), defining detailed system behavior, validation, evaluation states, error handling, security requirements, and testable acceptance criteria.