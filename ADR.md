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