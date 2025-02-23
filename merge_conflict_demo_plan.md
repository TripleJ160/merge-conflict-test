# Merge Conflict Demo Plan

## 1. Initial Setup
- Create a simple Python calculator app with basic operations
- Initialize git repository
- Create initial commit on main branch
- Create a development branch from main

## 2. Feature Branch Scenario
We'll create two feature branches from dev that will both modify the calculator app:

### Feature Branch 1: Enhanced Operations
- Create branch `feature/enhanced-ops` from dev
- Add power operation (x^y) to calculator
- Modify the main calculator function

### Feature Branch 2: Input Validation
- Create branch `feature/input-validation` from dev
- Add input validation to the same calculator function
- This will create a conflict since both branches modify the same function

## 3. Demonstrating the Conflict
1. Commit changes in both feature branches
2. Try to merge both features back into dev
3. Resolve the resulting merge conflict

## 4. Resolution Steps
1. Show how to identify merge conflicts in Git
2. Demonstrate how to use Git's conflict markers
3. Show best practices for resolving conflicts
4. Complete the merge after resolution

## 5. Best Practices
- Always pull latest dev before creating feature branches
- Communicate with team about which files are being modified
- Keep commits small and focused
- Use meaningful commit messages
- Test thoroughly after resolving conflicts

## Implementation Plan
1. Create the initial calculator.py with basic operations
2. Set up Git repository and branches
3. Make parallel changes in feature branches
4. Document each step of the conflict resolution process
5. Create a final working version that incorporates both features correctly