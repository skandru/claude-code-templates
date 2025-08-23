#!/usr/bin/env python3
"""
Claude Code Project Setup Automation
Creates optimal project structure 
"""

import os
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

class ClaudeProjectSetup:
    def __init__(self, project_name: str, project_path: Optional[str] = None):
        self.project_name = project_name
        self.project_path = Path(project_path) if project_path else Path.cwd() / project_name
        self.claude_dir = self.project_path / ".claude"
        self.docs_dir = self.project_path / "docs"
        self.agents_dir = self.claude_dir / "agents"
        
    def create_directory_structure(self):
        """Create the optimal directory structure"""
        directories = [
            self.project_path,
            self.claude_dir,
            self.agents_dir,
            self.docs_dir,
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory: {directory}")
    
    def create_claude_settings(self):
        """Create Claude Code security and permissions configuration"""
        settings = {
            "permissions": {
                "deny": [
                    "Read(./.env)",
                    "Read(./.env.*)",
                    "Read(./secrets/**)",
                    "Read(./config/credentials.json)",
                    "Read(./private/**)",
                    "Write(./.env)",
                    "Write(./.env.*)",
                    "Write(./secrets/**)"
                ],
                "allow": [
                    "Read(./docs/**)",
                    "Read(./src/**)",
                    "Read(./tests/**)",
                    "Write(./src/**)",
                    "Write(./tests/**)",
                    "Write(./docs/**)"
                ]
            },
            "context_limits": {
                "max_tokens": 150000,
                "compact_at_percent": 70,
                "warning_at_percent": 85
            },
            "project_settings": {
                "name": self.project_name,
                "created": datetime.now().isoformat(),
                "version": "1.0.0"
            }
        }
        
        settings_file = self.claude_dir / "settings.json"
        with open(settings_file, 'w') as f:
            json.dump(settings, f, indent=2)
        print(f"✅ Created Claude settings: {settings_file}")
    
    def create_specialized_agents(self):
        """Create the five specialized agents based on research"""
        agents = {
            "mvp-planner.md": self._get_mvp_planner_template(),
            "architect.md": self._get_architect_template(),
            "code-reviewer.md": self._get_code_reviewer_template(),
            "test-runner.md": self._get_test_runner_template(),
            "debugger.md": self._get_debugger_template()
        }
        
        for agent_name, template in agents.items():
            agent_file = self.agents_dir / agent_name
            with open(agent_file, 'w') as f:
                f.write(template)
            print(f"✅ Created agent: {agent_name}")
    
    def create_documentation_structure(self):
        """Create the documentation files based on research"""
        docs = {
            "01-scope.md": self._get_scope_template(),
            "02-decisions.md": self._get_decisions_template(),
            "03-tasks.md": self._get_tasks_template(),
            "architecture-design.md": self._get_architecture_template()
        }
        
        for doc_name, template in docs.items():
            doc_file = self.docs_dir / doc_name
            with open(doc_file, 'w') as f:
                f.write(template)
            print(f"✅ Created documentation: {doc_name}")
    
    def create_main_context_files(self):
        """Create CLAUDE.md and PLAYBOOK.md files"""
        claude_md = self.project_path / "CLAUDE.md"
        with open(claude_md, 'w') as f:
            f.write(self._get_claude_md_template())
        print(f"✅ Created main context: CLAUDE.md")
        
        playbook_md = self.project_path / "PLAYBOOK.md"
        with open(playbook_md, 'w') as f:
            f.write(self._get_playbook_template())
        print(f"✅ Created playbook: PLAYBOOK.md")
    
    def create_gitignore(self):
        """Create appropriate .gitignore file"""
        gitignore_content = """# Environment variables
.env
.env.*
!.env.example

# Secrets and credentials
secrets/
private/
config/credentials.json

# IDE and editor files
.vscode/
.idea/
*.swp
*.swo
*~

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
logs/
*.log

# Dependencies (language-specific - uncomment as needed)
# node_modules/
# __pycache__/
# *.pyc
# vendor/
# target/

# Build outputs
dist/
build/
*.egg-info/

# Claude Code specific (optional - keep these for team collaboration)
# .claude/settings.json
"""
        
        gitignore_file = self.project_path / ".gitignore"
        with open(gitignore_file, 'w') as f:
            f.write(gitignore_content)
        print(f"✅ Created .gitignore")
    
    def create_readme(self):
        """Create project README with Claude Code workflow instructions"""
        readme_content = f"""# {self.project_name}

## Claude Code Workflow

This project is set up with an optimized Claude Code workflow based on research-backed best practices.

### Quick Start

1. **Read the documentation first**:
   ```bash
   claude "Please read @docs/architecture-design.md and understand the project structure"
   ```

2. **Use the specialized agents**:
   - `@.claude/agents/mvp-planner.md` - For scope and planning
   - `@.claude/agents/architect.md` - For architecture decisions
   - `@.claude/agents/code-reviewer.md` - For code reviews
   - `@.claude/agents/test-runner.md` - For testing workflows
   - `@.claude/agents/debugger.md` - For debugging issues

3. **Follow the Explore-Plan-Code-Commit workflow**:
   - **Explore**: Have Claude read relevant files
   - **Plan**: Ask Claude to create a comprehensive plan
   - **Code**: Implement following the architecture
   - **Commit**: Create proper commits and update docs

### Key Commands

- `/context` - Check token usage
- `/compact` - Compress conversation history at 70% capacity
- `/clear` - Start fresh context for new features
- `@filepath` - Reference files without loading full content

### Project Structure

- `docs/` - Project documentation and specifications
- `.claude/` - Claude Code configuration and agents
- `CLAUDE.md` - Main project context (keep under 200 lines)
- `PLAYBOOK.md` - How this project works

## Development

[Add your project-specific development instructions here]

## Architecture

See `docs/architecture-design.md` for detailed architecture documentation.
"""
        
        readme_file = self.project_path / "README.md"
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        print(f"✅ Created README.md")

    # Template methods for all the files
    def _get_mvp_planner_template(self):
        return f"""# MVP Planner Agent

You are the MVP Planner for {self.project_name}. Your role is to convert vague goals into crisp scope with clear boundaries.

## Your Responsibilities

1. **Scope Definition**: Transform broad ideas into specific, measurable deliverables
2. **Boundary Setting**: Clearly define what's IN and OUT of scope
3. **Priority Ranking**: Order features by impact and feasibility
4. **Timeline Estimation**: Provide realistic development timelines
5. **Risk Assessment**: Identify potential blockers and dependencies

## Key Principles

- **Start Small**: Always push for the smallest viable first version
- **User-Focused**: Every feature must solve a real user problem
- **Measurable**: Define success criteria for each feature
- **Iterative**: Plan for multiple release cycles

## Planning Process

1. Ask clarifying questions about user needs
2. Break down features into specific user stories
3. Estimate complexity and dependencies
4. Create priority-ordered backlog
5. Define MVP vs. future iterations

## Templates to Use

### Feature Template
- **User Story**: As a [user], I want [goal] so that [benefit]
- **Acceptance Criteria**: Specific, testable conditions
- **Priority**: High/Medium/Low with justification
- **Effort**: T-shirt sizing (S/M/L/XL)
- **Dependencies**: What must be done first

### Scope Document Template
- **Project Goal**: One sentence describing the main objective
- **Target Users**: Who will use this and why
- **Core Features**: 3-5 essential features for MVP
- **Out of Scope**: What we're NOT building in v1
- **Success Metrics**: How we'll measure success

Remember: Your job is to prevent scope creep and ensure we build something users actually want.
"""

    def _get_architect_template(self):
        return f"""# Architect Agent

You are the Architect for {self.project_name}. Your role is to maintain architectural consistency and make sound technical decisions.

## Your Responsibilities

1. **System Design**: Create scalable, maintainable architecture
2. **Technology Decisions**: Choose appropriate tools and frameworks
3. **Code Standards**: Establish and enforce coding conventions
4. **Performance**: Ensure system meets performance requirements
5. **Security**: Build in security from the ground up

## Key Principles

- **KISS**: Keep it simple and straightforward
- **YAGNI**: You ain't gonna need it - avoid over-engineering
- **DRY**: Don't repeat yourself
- **SOLID**: Follow SOLID principles for object-oriented design
- **Separation of Concerns**: Each component has a single responsibility

## Architecture Review Checklist

### Before Implementation
- [ ] Does this align with the overall system architecture?
- [ ] Are we using established patterns and conventions?
- [ ] Is this the simplest solution that meets requirements?
- [ ] Are dependencies minimal and well-justified?

### During Code Review
- [ ] Is the code structure clean and logical?
- [ ] Are naming conventions followed?
- [ ] Is error handling appropriate?
- [ ] Are there adequate tests?
- [ ] Is performance acceptable?

### System Design Considerations
- **Scalability**: How will this perform under load?
- **Maintainability**: Can future developers easily understand this?
- **Testability**: Is the code easy to test?
- **Security**: Are there any security vulnerabilities?
- **Monitoring**: How will we observe this in production?

## Documentation Standards

- **Architecture Decisions**: Record all significant decisions with rationale
- **API Documentation**: Clear, complete API documentation
- **Setup Instructions**: Anyone should be able to run the project locally
- **Deployment Guide**: Clear deployment and configuration instructions

## Common Patterns to Enforce

1. **Repository Pattern**: For data access abstraction
2. **Factory Pattern**: For object creation
3. **Observer Pattern**: For event-driven architecture
4. **Decorator Pattern**: For extending functionality
5. **Strategy Pattern**: For algorithmic variations

Remember: Your job is to ensure the system is built right, not just that it works.
"""

    def _get_code_reviewer_template(self):
        return f"""# Code Reviewer Agent

You are the Code Reviewer for {self.project_name}. Your role is to perform comprehensive quality and security reviews.

## Your Responsibilities

1. **Code Quality**: Ensure code meets standards and best practices
2. **Security Review**: Identify potential security vulnerabilities
3. **Performance Analysis**: Check for performance issues
4. **Test Coverage**: Verify adequate testing
5. **Documentation**: Ensure code is properly documented

## Review Checklist

### Code Quality
- [ ] Code follows established style guidelines
- [ ] Functions/methods have single responsibility
- [ ] Variable and function names are descriptive
- [ ] No code duplication (DRY principle)
- [ ] Error handling is comprehensive
- [ ] Edge cases are handled
- [ ] Code is readable and well-commented

### Security Review
- [ ] Input validation is present
- [ ] SQL injection prevention
- [ ] XSS prevention measures
- [ ] Authentication/authorization checks
- [ ] Sensitive data is properly handled
- [ ] No hardcoded secrets
- [ ] HTTPS/TLS properly configured

### Performance
- [ ] Database queries are optimized
- [ ] No N+1 query problems
- [ ] Appropriate caching strategies
- [ ] Resource cleanup (connections, files, etc.)
- [ ] Memory usage is reasonable
- [ ] Algorithms are efficient

### Testing
- [ ] Unit tests cover core functionality
- [ ] Integration tests for key workflows
- [ ] Edge cases are tested
- [ ] Error conditions are tested
- [ ] Tests are fast and reliable
- [ ] Test coverage meets requirements

### Documentation
- [ ] Public APIs are documented
- [ ] Complex logic has explanatory comments
- [ ] README is up to date
- [ ] Architecture decisions are recorded

## Common Issues to Flag

1. **Security Vulnerabilities**
   - Unvalidated input
   - Hardcoded credentials
   - Improper access controls
   - Information disclosure

2. **Performance Problems**
   - Inefficient database queries
   - Memory leaks
   - Blocking operations
   - Poor caching

3. **Maintainability Issues**
   - God classes/functions
   - High coupling
   - Poor abstraction
   - Inconsistent patterns

## Review Comments Template

**Severity Levels**:
- 🔴 **Blocker**: Must fix before merge
- 🟡 **Major**: Should fix before merge
- 🔵 **Minor**: Consider fixing
- 💡 **Suggestion**: Optional improvement

**Comment Format**:
```
[Severity] Issue description

Explanation of why this is a problem.

Suggested solution or alternative approach.
```

Remember: Your job is to catch issues before they reach production and help maintain code quality.
"""

    def _get_test_runner_template(self):
        return f"""# Test Runner Agent

You are the Test Runner for {self.project_name}. Your role is to automate testing workflows and ensure comprehensive test coverage.

## Your Responsibilities

1. **Test Strategy**: Define comprehensive testing approach
2. **Test Automation**: Create and maintain automated test suites
3. **Coverage Analysis**: Ensure adequate test coverage
4. **Performance Testing**: Validate system performance
5. **CI/CD Integration**: Integrate tests into deployment pipeline

## Testing Strategy

### Test Pyramid
1. **Unit Tests** (70%)
   - Test individual functions/methods
   - Fast execution (<1ms per test)
   - Isolated and independent
   - Mock external dependencies

2. **Integration Tests** (20%)
   - Test component interactions
   - Database and API integrations
   - End-to-end workflows
   - Real dependencies where appropriate

3. **E2E Tests** (10%)
   - User journey testing
   - Browser automation
   - Full system validation
   - Production-like environment

### Test Categories

**Functional Testing**
- [ ] Happy path scenarios
- [ ] Edge cases and boundary conditions
- [ ] Error handling and recovery
- [ ] Input validation

**Non-Functional Testing**
- [ ] Performance and load testing
- [ ] Security testing
- [ ] Accessibility testing
- [ ] Cross-browser/platform testing

**Regression Testing**
- [ ] Automated regression suite
- [ ] Smoke tests for critical paths
- [ ] Database migration testing
- [ ] API backward compatibility

## Test Automation Framework

### Unit Testing
```bash
# Run unit tests
npm test
# or
pytest
# or
go test ./...
```

### Integration Testing
```bash
# Run integration tests
npm run test:integration
# or
pytest tests/integration/
```

### E2E Testing
```bash
# Run end-to-end tests
npm run test:e2e
# or
pytest tests/e2e/
```

## Quality Gates

### Pre-Commit Checks
- [ ] All tests pass
- [ ] Code coverage > 80%
- [ ] Linting passes
- [ ] Security scan passes

### Pre-Release Checks
- [ ] Full test suite passes
- [ ] Performance benchmarks met
- [ ] Security scan clean
- [ ] Manual QA complete

## Test Data Management

1. **Test Fixtures**: Reusable test data sets
2. **Test Factories**: Generate test data programmatically
3. **Database Seeding**: Consistent test database state
4. **Mock Services**: Simulate external dependencies

## Continuous Testing

### CI Pipeline Integration
```yaml
# Example GitHub Actions workflow
test:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v2
    - name: Run Tests
      run: |
        npm install
        npm run test:all
        npm run test:coverage
```

### Monitoring and Alerts
- Test failure notifications
- Coverage regression alerts
- Performance degradation warnings
- Flaky test identification

## Test Metrics to Track

- **Coverage**: Line, branch, and function coverage
- **Execution Time**: Test suite performance
- **Flakiness**: Inconsistent test results
- **Defect Escape Rate**: Bugs found in production

Remember: Your job is to catch bugs before users do and maintain confidence in our deployments.
"""

    def _get_debugger_template(self):
        return f"""# Debugger Agent

You are the Debugger for {self.project_name}. Your role is to systematically diagnose and resolve issues.

## Your Responsibilities

1. **Issue Diagnosis**: Identify root causes of problems
2. **Systematic Debugging**: Use structured approach to problem-solving
3. **Log Analysis**: Interpret logs and error messages
4. **Performance Debugging**: Identify and fix performance bottlenecks
5. **Production Support**: Handle live system issues

## Debugging Methodology

### 1. Problem Definition
- **Reproduce the Issue**: Can you consistently reproduce it?
- **Scope Assessment**: How widespread is the problem?
- **Impact Analysis**: Who/what is affected?
- **Urgency Level**: Critical/High/Medium/Low

### 2. Information Gathering
- **Error Messages**: Collect all relevant error logs
- **System State**: Check system resources, database connections
- **Recent Changes**: What changed recently?
- **User Actions**: What steps led to the issue?

### 3. Hypothesis Formation
- **Potential Causes**: List possible root causes
- **Priority Order**: Most likely causes first
- **Test Strategy**: How to verify each hypothesis

### 4. Systematic Testing
- **Isolated Testing**: Test one change at a time
- **Control Variables**: Change only what you're testing
- **Document Results**: Keep detailed notes

### 5. Root Cause Analysis
- **Five Whys**: Ask "why" five times to find root cause
- **Fishbone Diagram**: Categorize potential causes
- **Timeline Analysis**: When did the problem start?

## Common Debugging Scenarios

### Application Crashes
```bash
# Check logs
tail -f /var/log/application.log

# Check system resources
top
df -h
free -m

# Check process status
ps aux | grep application
```

### Performance Issues
```bash
# Profile CPU usage
top -p <pid>

# Profile memory usage
valgrind --tool=memcheck ./application

# Check database performance
EXPLAIN ANALYZE SELECT ...
```

### Database Problems
```sql
-- Check slow queries
SELECT * FROM performance_schema.events_statements_summary_by_digest
ORDER BY avg_timer_wait DESC;

-- Check locks
SHOW PROCESSLIST;
```

### Network Issues
```bash
# Check connectivity
ping hostname
telnet hostname port

# Check DNS resolution
nslookup hostname

# Check network traffic
netstat -tulpn
```

## Debugging Tools Checklist

### Logging
- [ ] Structured logging (JSON format)
- [ ] Appropriate log levels
- [ ] Correlation IDs for request tracing
- [ ] Log aggregation and search

### Monitoring
- [ ] Application metrics
- [ ] System metrics (CPU, memory, disk)
- [ ] Custom business metrics
- [ ] Alerting rules

### Profiling
- [ ] CPU profiling tools
- [ ] Memory profiling tools
- [ ] Database query profiling
- [ ] Network request tracing

### Local Development
- [ ] Debugger setup (breakpoints, step-through)
- [ ] Hot reloading for fast iteration
- [ ] Local environment mirrors production
- [ ] Test data that reproduces issues

## Emergency Response Playbook

### Severity 1 (Critical)
1. **Immediate**: Acknowledge incident
2. **5 min**: Initial assessment and communication
3. **15 min**: Implement quick fix or rollback
4. **30 min**: Detailed root cause analysis begins
5. **Post-incident**: Full retrospective and prevention

### Communication Template
```
Incident: [Brief description]
Status: [Investigating/Identified/Monitoring/Resolved]
Impact: [Who/what is affected]
ETA: [When we expect resolution]
Next Update: [When we'll provide next update]
```

## Prevention Strategies

1. **Better Testing**: Add tests that would have caught this
2. **Monitoring**: Add alerts for similar issues
3. **Code Review**: Update review checklist
4. **Documentation**: Update runbooks and procedures

## Knowledge Base

Maintain a searchable knowledge base of:
- Common issues and solutions
- Debugging procedures
- System architecture diagrams
- Contact information for dependencies

Remember: Your job is to solve problems quickly and prevent them from happening again.
"""

    def _get_scope_template(self):
        return f"""# Project Scope: {self.project_name}

## Project Overview

**Project Goal**: [One sentence describing the main objective]

**Target Users**: [Who will use this and why]

**Project Timeline**: [Estimated duration and key milestones]

## Core Features (MVP)

### Feature 1: [Name]
- **User Story**: As a [user], I want [goal] so that [benefit]
- **Acceptance Criteria**: 
  - [ ] Specific, testable condition 1
  - [ ] Specific, testable condition 2
  - [ ] Specific, testable condition 3
- **Priority**: High/Medium/Low
- **Effort Estimate**: S/M/L/XL

### Feature 2: [Name]
- **User Story**: As a [user], I want [goal] so that [benefit]
- **Acceptance Criteria**: 
  - [ ] Specific, testable condition 1
  - [ ] Specific, testable condition 2
- **Priority**: High/Medium/Low
- **Effort Estimate**: S/M/L/XL

[Add more features as needed]

## Out of Scope (V1)

List what we're NOT building in the first version:
- [ ] Advanced feature that can wait
- [ ] Nice-to-have functionality
- [ ] Complex integrations for later

## Success Metrics

How we'll measure success:
- **Primary Metric**: [Main KPI]
- **Secondary Metrics**: 
  - [Supporting metric 1]
  - [Supporting metric 2]
- **User Satisfaction**: [How we'll measure this]

## Constraints and Assumptions

### Technical Constraints
- [Technology limitations]
- [Performance requirements]
- [Security requirements]

### Business Constraints
- [Budget limitations]
- [Time constraints]
- [Resource availability]

### Assumptions
- [Key assumptions we're making]
- [Dependencies on external factors]

## Risk Assessment

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|-------------------|
| [Risk description] | High/Medium/Low | High/Medium/Low | [How we'll handle it] |

## Stakeholder Sign-off

- [ ] Product Owner: [Name]
- [ ] Technical Lead: [Name]
- [ ] Business Sponsor: [Name]

---
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}
**Next Review**: [Date for next scope review]
"""

    def _get_decisions_template(self):
        return f"""# Architecture Decision Log: {self.project_name}

This document tracks all significant architectural decisions made during the project.

## Decision Template

For each decision, use this format:

### ADR-XXX: [Decision Title]

**Date**: [YYYY-MM-DD]
**Status**: [Proposed/Accepted/Deprecated/Superseded]
**Deciders**: [List of people involved in the decision]

**Context**
What is the issue that we're seeing that is motivating this decision or change?

**Decision**
What is the change that we're proposing or have agreed to implement?

**Consequences**
What becomes easier or more difficult to do and any risks introduced by this change?

---

## Current Decisions

### ADR-001: Initial Technology Stack

**Date**: {datetime.now().strftime('%Y-%m-%d')}
**Status**: Proposed
**Deciders**: [Team members]

**Context**
We need to choose the core technology stack for this project, considering factors like team expertise, scalability requirements, and development speed.

**Decision**
[Document your technology choices here]
- **Backend**: [Language/Framework and why]
- **Frontend**: [Framework and why]  
- **Database**: [Database choice and why]
- **Infrastructure**: [Deployment platform and why]

**Consequences**
- **Positive**: [Benefits of this choice]
- **Negative**: [Limitations or risks]
- **Neutral**: [Other considerations]

### ADR-002: [Next Decision]

**Date**: [Date]
**Status**: [Status]
**Deciders**: [Names]

**Context**
[Context for the decision]

**Decision**
[What was decided]

**Consequences**
[Impact of the decision]

---

## Decision Categories

Track decisions by category:

### Technical Architecture
- Technology stack choices
- System architecture patterns
- Database design decisions
- API design approaches

### Security
- Authentication strategy
- Authorization model
- Data encryption decisions
- Security framework choices

### Performance
- Caching strategies
- Database optimization approaches
- CDN and asset delivery
- Monitoring and observability

### DevOps
- Deployment strategy
- CI/CD pipeline design
- Infrastructure as code approach
- Monitoring and alerting

### User Experience
- UI/UX framework decisions
- Accessibility approach
- Mobile responsiveness strategy
- Internationalization plans

---

**Review Schedule**: Monthly review of all decisions
**Next Review**: [Date]
"""

    def _get_tasks_template(self):
        return f"""# Task Checklist: {self.project_name}

## Current Sprint/Iteration

**Sprint Goal**: [What we want to accomplish this iteration]
**Start Date**: [Date]
**End Date**: [Date]

### In Progress
- [ ] **[Task Name]** - @assigned-person
  - **Status**: In Progress
  - **Description**: [Brief description]
  - **Blocked By**: [Any blockers]
  
### To Do (Prioritized)
- [ ] **[High Priority Task]** - Priority: High
  - **Description**: [What needs to be done]
  - **Acceptance Criteria**: [How we know it's done]
  - **Estimated Effort**: [S/M/L/XL]
  
- [ ] **[Medium Priority Task]** - Priority: Medium
  - **Description**: [What needs to be done]
  - **Dependencies**: [What needs to be done first]

### Blocked
- [ ] **[Blocked Task]**
  - **Blocked By**: [What's blocking progress]
  - **Action Needed**: [What needs to happen to unblock]

### Done ✅
- [x] **[Completed Task]** - Completed on [Date]

## Backlog

### High Priority (Next Sprint)
- [ ] [Task for next iteration]
- [ ] [Another task for next iteration]

### Medium Priority (Future)
- [ ] [Future enhancement]
- [ ] [Nice-to-have feature]

### Low Priority (Maybe)
- [ ] [Optional improvement]
- [ ] [Far future consideration]

## Technical Debt

Track technical debt items that need attention:
- [ ] **[Tech Debt Item]**
  - **Impact**: [How it affects development]
  - **Effort to Fix**: [Estimated effort]
  - **Priority**: [When to address]

## Bugs

Track and prioritize bug fixes:
- [ ] **[Bug Description]** - Severity: [Critical/High/Medium/Low]
  - **Steps to Reproduce**: [How to reproduce]
  - **Expected**: [What should happen]
  - **Actual**: [What actually happens]
  - **Environment**: [Where it occurs]

## Dependencies

Track external dependencies:
- [ ] **[Dependency]**
  - **Depends On**: [External team/system/decision]
  - **Expected Date**: [When we expect resolution]
  - **Contact**: [Who to follow up with]

## Retrospective Items

Things to discuss in the next retrospective:
- **What Went Well**: [Positive items to continue]
- **What Could Improve**: [Areas for improvement]  
- **Action Items**: [Specific actions to take]

## Meeting Actions

Track action items from meetings:
- [ ] **[Action Item]** - @responsible-person
  - **From Meeting**: [Meeting name/date]
  - **Due Date**: [When it's due]

---

**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}
**Next Review**: [Next sprint planning date]
"""

    def _get_architecture_template(self):
        return f"""# Architecture Design: {self.project_name}

## System Overview

**Purpose**: [High-level description of what this system does]

**Key Requirements**:
- [Functional requirement 1]
- [Functional requirement 2]
- [Non-functional requirement 1]
- [Non-functional requirement 2]

## Architecture Principles

1. **Simplicity**: Keep the architecture as simple as possible
2. **Scalability**: Design for growth and increased load
3. **Maintainability**: Code should be easy to understand and modify
4. **Security**: Security considerations built into every layer
5. **Performance**: Meet performance requirements efficiently

## System Architecture

### High-Level Architecture

```
[Insert architecture diagram description or ASCII art]

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Client    │    │     API     │    │  Database   │
│ (Frontend)  │◄──►│  (Backend)  │◄──►│   Server    │
└─────────────┘    └─────────────┘    └─────────────┘
```

### Component Overview

#### Frontend Layer
- **Technology**: [Framework/Library]
- **Responsibilities**: User interface, client-side logic, API communication
- **Key Patterns**: [Architecture patterns used]

#### Backend Layer  
- **Technology**: [Language/Framework]
- **Responsibilities**: Business logic, API endpoints, data validation
- **Key Patterns**: [Architecture patterns used]

#### Data Layer
- **Technology**: [Database type]
- **Responsibilities**: Data persistence, query optimization, backup
- **Key Patterns**: [Data access patterns]

## Detailed Design

### API Design

**API Style**: REST/GraphQL/RPC
**Base URL**: [API base URL]
**Authentication**: [Auth method]

#### Key Endpoints
- `GET /api/[resource]` - [Description]
- `POST /api/[resource]` - [Description]  
- `PUT /api/[resource]/:id` - [Description]
- `DELETE /api/[resource]/:id` - [Description]

### Database Design

#### Core Entities
- **[Entity 1]**: [Description and key attributes]
- **[Entity 2]**: [Description and key attributes]
- **[Entity 3]**: [Description and key attributes]

#### Relationships
- [Entity 1] → [Entity 2]: [Relationship description]
- [Entity 2] → [Entity 3]: [Relationship description]

### Security Architecture

#### Authentication
- **Method**: [JWT/Session/OAuth/etc.]
- **Flow**: [Authentication flow description]
- **Token Management**: [How tokens are handled]

#### Authorization  
- **Model**: [RBAC/ABAC/etc.]
- **Implementation**: [How permissions are checked]

#### Data Protection
- **Encryption**: [At rest and in transit]
- **Input Validation**: [Validation strategy]
- **Output Sanitization**: [XSS prevention]

## Deployment Architecture

### Environment Strategy
- **Development**: [Local development setup]
- **Staging**: [Pre-production environment]
- **Production**: [Live environment]

### Infrastructure
- **Hosting**: [Cloud provider/platform]
- **Containerization**: [Docker/Kubernetes strategy]
- **Database**: [Database hosting and scaling]
- **CDN**: [Content delivery network]

### CI/CD Pipeline
1. **Code Commit** → Automated tests
2. **Tests Pass** → Build artifacts  
3. **Build Success** → Deploy to staging
4. **Staging Validation** → Deploy to production
5. **Production Deploy** → Health checks

## Performance Considerations

### Scalability
- **Horizontal Scaling**: [How to scale out]
- **Vertical Scaling**: [How to scale up]
- **Database Scaling**: [Read replicas, sharding, etc.]

### Caching Strategy
- **Application Cache**: [In-memory caching]
- **Database Cache**: [Query result caching]
- **CDN Cache**: [Static asset caching]

### Monitoring
- **Application Metrics**: [What we measure]
- **Infrastructure Metrics**: [System monitoring]
- **Business Metrics**: [KPI tracking]

## Error Handling

### Error Response Format
```json
{{
  "error": {{
    "code": "ERROR_CODE",
    "message": "User-friendly message",
    "details": "Technical details for debugging"
  }}
}}
```

### Logging Strategy
- **Log Levels**: DEBUG, INFO, WARN, ERROR
- **Log Format**: Structured JSON logging
- **Log Aggregation**: [Centralized logging system]

## Testing Strategy

### Unit Testing
- **Coverage Target**: 80%+ line coverage
- **Framework**: [Testing framework]
- **Mock Strategy**: [How external dependencies are mocked]

### Integration Testing
- **API Testing**: [API test approach]
- **Database Testing**: [Data layer testing]
- **End-to-End Testing**: [E2E test strategy]

## Future Considerations

### Planned Enhancements
- [Feature enhancement 1]
- [Feature enhancement 2]
- [Performance improvement 1]

### Technical Debt
- [Known technical debt item 1]
- [Known technical debt item 2]

### Scaling Concerns
- [When we'll need to address scaling]
- [Potential bottlenecks to monitor]

---

**Document Version**: 1.0
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}
**Next Review**: [Review date]
**Reviewers**: [Names of reviewers needed]
"""

    def _get_claude_md_template(self):
        return f"""# {self.project_name}

## Project Context

**Purpose**: [Brief description of what this project does]
**Status**: [In Development/Testing/Production]
**Team**: [Team members and roles]

## Quick Start

1. **Read First**: `@docs/architecture-design.md` for technical overview
2. **Development Setup**: [Key setup steps]  
3. **Key Commands**: [Most common development commands]

## Architecture Summary

- **Frontend**: [Technology and key patterns]
- **Backend**: [Technology and key patterns]
- **Database**: [Database and key design decisions]
- **Deployment**: [How this is deployed]

## Current Focus

**This Sprint**: [Current iteration goals]
**Next Up**: [What's coming next]
**Blockers**: [Any current blockers]

## Key Files and Folders

- `docs/` - All project documentation
- `src/` - Source code
- `tests/` - Test files
- `.claude/agents/` - Specialized Claude agents

## Workflow Reminders

### Use the Agents
- **Planning**: `@.claude/agents/mvp-planner.md`
- **Architecture**: `@.claude/agents/architect.md`  
- **Review**: `@.claude/agents/code-reviewer.md`
- **Testing**: `@.claude/agents/test-runner.md`
- **Debug**: `@.claude/agents/debugger.md`

### Best Practices
- Follow **Explore-Plan-Code-Commit** workflow
- Use `/context` to monitor token usage
- Use `/compact` at 70% capacity
- Use `/clear` between major feature work
- Reference files with `@filepath` when possible

## Recent Decisions

[Link to key recent architecture decisions]

## Common Commands

```bash
# Development
[key development commands]

# Testing  
[key testing commands]

# Deployment
[key deployment commands]
```

---
*Keep this file under 200 lines. For detailed info, reference docs/ files.*
"""

    def _get_playbook_template(self):
        return f"""# {self.project_name} Playbook

## How This Project Works

This playbook explains how to effectively work on {self.project_name} using our optimized Claude Code workflow.

## Getting Started

### Prerequisites
- [List required tools and versions]
- [Environment setup requirements]
- [Access requirements]

### Initial Setup
```bash
# Clone and setup
git clone [repository-url]
cd {self.project_name}
[setup commands]
```

### Claude Code Integration
```bash
# Start Claude Code session
claude --dangerously-skip-permissions

# First interaction
claude "Please read @docs/architecture-design.md and @CLAUDE.md to understand this project"
```

## Development Workflow

### 1. Explore Phase
Before starting any work:
```bash
claude "Please read @docs/03-tasks.md and show me current sprint tasks"
claude "Read relevant files for [feature] and understand the current implementation"
```

### 2. Plan Phase  
For any new feature:
```bash
claude "Act as @.claude/agents/mvp-planner.md and help me plan [feature]"
claude "Act as @.claude/agents/architect.md and review this plan for [feature]"
```

### 3. Code Phase
During implementation:
```bash
claude "Implement [feature] following our architecture in @docs/architecture-design.md"
claude "Act as @.claude/agents/code-reviewer.md and review the implementation"
```

### 4. Commit Phase
After implementation:
```bash
claude "Act as @.claude/agents/test-runner.md and create tests for [feature]"
claude "Help me create a proper commit message and update relevant documentation"
```

## Specialized Agents

### MVP Planner (`@.claude/agents/mvp-planner.md`)
**Use When**: Planning new features, defining scope, prioritizing work
**Prompt**: "Act as the MVP Planner and help me [specific planning task]"

### Architect (`@.claude/agents/architect.md`)  
**Use When**: Making technical decisions, reviewing system design
**Prompt**: "Act as the Architect and review [architectural decision/code]"

### Code Reviewer (`@.claude/agents/code-reviewer.md`)
**Use When**: Before committing code, during code reviews
**Prompt**: "Act as the Code Reviewer and review [specific files/changes]"

### Test Runner (`@.claude/agents/test-runner.md`)
**Use When**: Creating tests, running test suites, debugging test failures
**Prompt**: "Act as the Test Runner and help me [testing task]"

### Debugger (`@.claude/agents/debugger.md`)
**Use When**: Investigating bugs, performance issues, system problems
**Prompt**: "Act as the Debugger and help me diagnose [specific problem]"

## Context Management

### Monitor Usage
```bash
# Check current token usage
/context

# Compact conversation when needed (at ~70%)  
/compact

# Clear context for new major feature
/clear
```

### File References
```bash
# Reference without loading full content
claude "Based on @docs/architecture-design.md, implement [feature]"

# Load and analyze specific files
claude "Read and analyze src/components/UserAuth.js"
```

## Common Scenarios

### Starting a New Feature
1. `claude "/clear"`
2. `claude "Read @CLAUDE.md and @docs/architecture-design.md"`
3. `claude "Act as @.claude/agents/mvp-planner.md and help me plan [feature]"`
4. Follow Explore-Plan-Code-Commit workflow

### Debugging an Issue
1. `claude "Act as @.claude/agents/debugger.md"`
2. `claude "Help me diagnose [specific issue with details]"`
3. Follow the systematic debugging approach

### Code Review  
1. `claude "Act as @.claude/agents/code-reviewer.md"`
2. `claude "Review the following changes: [describe changes]"`
3. Address feedback and re-review if needed

### Performance Optimization
1. `claude "Act as @.claude/agents/architect.md"`
2. `claude "Review performance bottlenecks in [specific area]"`
3. `claude "Act as @.claude/agents/test-runner.md and create performance tests"`

## Quality Gates

### Before Committing
- [ ] Code review by Code Reviewer agent
- [ ] Tests created and passing (Test Runner agent)  
- [ ] Architecture review if needed (Architect agent)
- [ ] Documentation updated

### Before Releasing
- [ ] Full test suite passes
- [ ] Performance benchmarks met
- [ ] Security review complete
- [ ] Documentation up to date

## Troubleshooting

### Claude Code Issues
- **High token usage**: Use `/compact` or `/clear`
- **Context confusion**: Start fresh with `/clear` and reload key docs
- **Permission errors**: Check `.claude/settings.json`

### Development Issues
- **Build failures**: Check environment setup and dependencies
- **Test failures**: Use Test Runner agent for systematic debugging
- **Performance issues**: Use Architect and Debugger agents

## Team Collaboration

### Sharing Context
When asking teammates for help:
1. Share relevant files from `docs/` folder
2. Reference the specific agent conversation
3. Include current task from `docs/03-tasks.md`

### Onboarding New Team Members
1. Have them read this playbook
2. Walk through the agent-based workflow
3. Pair on first few features using the workflow

## Continuous Improvement

### Weekly Review
- Review agent effectiveness
- Update documentation based on learnings
- Identify workflow improvements

### Monthly Architecture Review
- Review `docs/02-decisions.md`
- Update `docs/architecture-design.md` as needed
- Assess technical debt in `docs/03-tasks.md`

---

**Remember**: The agents are your specialized consultants. Use them actively and trust their expertise in their domains.
"""

    def setup_project(self):
        """Run the complete project setup"""
        print(f"🚀 Setting up Claude Code project: {self.project_name}")
        print(f"📁 Project path: {self.project_path}")
        print()
        
        try:
            self.create_directory_structure()
            self.create_claude_settings()
            self.create_specialized_agents()
            self.create_documentation_structure()
            self.create_main_context_files()
            self.create_gitignore()
            self.create_readme()
            
            print()
            print("✅ Claude Code project setup complete!")
            print()
            print("🎯 Next steps:")
            print(f"1. cd {self.project_path}")
            print("2. Initialize git: git init")
            print("3. Edit docs/architecture-design.md with your project specifics")
            print("4. Start Claude Code: claude --dangerously-skip-permissions")
            print("5. Begin with: claude \"Please read @CLAUDE.md and @docs/architecture-design.md\"")
            print()
            print("📚 Key files to customize:")
            print("- docs/01-scope.md (define your project scope)")
            print("- docs/architecture-design.md (your technical architecture)")
            print("- CLAUDE.md (keep under 200 lines)")
            print()
            
        except Exception as e:
            print(f"❌ Error during setup: {e}")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Setup optimal Claude Code project structure",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python claude_setup.py my-awesome-app
  python claude_setup.py my-app --path /path/to/projects/
  python claude_setup.py api-service --path ~/dev/
        """
    )
    
    parser.add_argument(
        'project_name',
        help='Name of the project to create'
    )
    
    parser.add_argument(
        '--path',
        help='Parent directory where project should be created (default: current directory)',
        default=None
    )
    
    args = parser.parse_args()
    
    # Validate project name
    if not args.project_name.replace('-', '').replace('_', '').isalnum():
        print("❌ Project name should contain only letters, numbers, hyphens, and underscores")
        sys.exit(1)
    
    # Setup the project
    setup = ClaudeProjectSetup(args.project_name, args.path)
    setup.setup_project()


if __name__ == "__main__":
    main()