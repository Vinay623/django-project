# Architecture Decision Records

## ADR 1: Use Enrolment Model for Relationship

Status: Accepted

### Context
We needed to store student-course relationships with semester and year.

### Alternatives considered
1. ManyToManyField
   - Simple but no extra fields
2. Separate model
   - Supports extra fields

### Decision
We used a separate Enrolment model.

### Code reference
enrolment/models.py

### Consequences
More flexible and scalable design


## ADR 2: Use Class-Based Views

Status: Accepted

### Context
We needed to handle display and creation of records.

### Alternatives
1. Function-based views
2. Class-based views

### Decision
Used class-based views for reusable code.

### Code reference
enrolment/views.py


## ADR 3: Use ModelForms

Status: Accepted

### Context
Forms needed for user input.

### Decision
Used ModelForms for automatic validation.

### Code reference
enrolment/forms.py
## ADR 4: Django Design Philosophy

Status: Accepted

### Context
Django follows "Don't Repeat Yourself (DRY)" and "Convention over Configuration".

### Decision
We used ModelForms and class-based views to reduce repeated code.

### Consequences
Cleaner and maintainable codebase.
## ADR 5: Use QuerySet API

Status: Accepted

### Context
Need to retrieve data efficiently.

### Decision
Used Django QuerySet API for filtering and retrieving data.

### Code reference
enrolment/views.py

### Consequences
Efficient database interaction.