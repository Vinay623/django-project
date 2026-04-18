ADR 1: Use Enrolment Model for Student–Course Relationship

Status: Accepted

Context

The system needs to store the relationship between students and courses. A student can enrol in many courses, and a course can have many students. The project also requires extra information for each enrolment, such as semester and year.

Alternatives Considered

1. ManyToManyField

Simple to implement
Suitable for basic many-to-many relationships
Not suitable when extra fields like semester and year are required

2. Separate Enrolment Model

Supports extra attributes
Makes the relationship explicit
Easier to extend later
Decision

We decided to use a separate Enrolment model to represent the many-to-many relationship between Student and Course.

Code Reference

enrolment/models.py

Consequences

This design improves flexibility and scalability. It allows the system to store additional enrolment details and follows object-oriented design more clearly.

ADR 2: Use Class-Based Views

Status: Accepted

Context

The application needs views for displaying records and creating new records. The design should be reusable, organised, and aligned with Django best practices.

Alternatives Considered

1. Function-Based Views

Easy for small applications
More direct and simple for beginners
Can become repetitive as the project grows

2. Class-Based Views

Reusable and structured
Reduce repeated code
Easier to extend for common tasks such as list and create operations
Decision

We decided to use class-based views because they provide better code reuse and cleaner structure for handling repeated patterns in the application.

Code Reference

enrolment/views.py

Consequences

This improves maintainability and supports Django’s reusable design style. It also helps organise logic more clearly.

ADR 3: Use ModelForms for User Input

Status: Accepted

Context

The system requires forms to create and validate student, course, and enrolment data. Manual validation would increase code repetition and the chance of errors.

Alternatives Considered

1. Manual HTML Forms

Full control over form handling
Requires custom validation and more repeated code

2. Django ModelForms

Automatically connects forms to models
Provides built-in validation
Reduces development time
Decision

We decided to use Django ModelForms for handling user input and validation.

Code Reference

enrolment/forms.py

Consequences

This reduces boilerplate code, improves reliability, and supports Django’s DRY principle.

ADR 4: Apply Django Design Philosophy (DRY and Separation of Concerns)

Status: Accepted

Context

The project should follow Django design principles to keep the code organised, readable, and maintainable.

Alternatives Considered

1. Mixed logic across templates, views, and forms

Faster initially
Harder to maintain and debug

2. Clear separation using models, forms, views, and templates

Better organisation
Easier to test and extend
Matches Django philosophy
Decision

We decided to separate responsibilities across models, forms, views, and templates, while following the DRY principle to avoid unnecessary repetition.

Code Reference

enrolment/models.py
enrolment/views.py
enrolment/forms.py

Consequences

This creates a cleaner and more maintainable codebase. It also demonstrates good software design practice.

ADR 5: Use Django QuerySet API for Data Access

Status: Accepted

Context

The application needs a reliable and readable way to retrieve, filter, and display database records.

Alternatives Considered

1. Raw SQL

More control
Harder to maintain
Less readable for this project

2. Django QuerySet API

Safer and more readable
Integrated with Django ORM
Easier to maintain and extend
Decision

We decided to use Django’s QuerySet API for retrieving and filtering application data.

Code Reference

enrolment/views.py

Consequences

This improves readability, reduces database handling complexity, and supports efficient interaction with the database.
