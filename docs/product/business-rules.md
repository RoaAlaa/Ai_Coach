Business rules
Here is our current agreed baseline.
ID	Business rule
BR-01	A user can have multiple interview attempts.
BR-02	A question set can contain multiple questions, and a question can be reused across sets.
BR-03	Draft question sets can be edited; published sets are immutable.
BR-04	Changing a question means creating a new question record.
BR-05	An attempt can be paused and resumed before submission.
BR-06	Submission locks the attempt and its answers.
BR-07	An attempt may be submitted with unanswered questions.
BR-08	Evaluation covers answered questions and reports how many questions were completed.
BR-09	Failed evaluations can be retried using the same submitted answers. Each retry creates a new evaluation record.
BR-10	Each attempt has one persistent conversation for discussing its questions, answers, and evaluation.
BR-11	Voice answers are transcribed into text; the answer records the submission type.
BR-12	Historical attempts retain the original question set and question content they used.