# Understanding and Resolving Merge Conflicts

This guide demonstrates a practical example of how merge conflicts occur and how to resolve them, using our calculator project as an example.

## What We Did

1. **Initial Setup**
   - Created a basic calculator with add, subtract, multiply, and divide operations
   - Initialized git repository and created main branch
   - Created development (dev) branch

2. **Feature Branches**
   - Created two feature branches from dev:
     * `feature/enhanced-ops`: Added power operation
     * `feature/input-validation`: Added input validation

3. **Conflict Occurred Because**
   - Both branches modified the same `calculator()` function
   - `feature/enhanced-ops` added a new operation
   - `feature/input-validation` added validation logic
   - Git couldn't automatically merge these changes

## How to Handle Merge Conflicts

1. **Prevention**
   - Always pull latest dev before creating feature branches
   - Communicate with team about which files are being modified
   - Keep commits small and focused
   - Regular merges from dev into feature branches

2. **When Conflict Occurs**
   ```bash
   # You'll see something like:
   Auto-merging calculator.py
   CONFLICT (content): Merge conflict in calculator.py
   Automatic merge failed; fix conflicts and then commit the result.
   ```

3. **Understanding Conflict Markers**
   ```python
   <<<<<<< HEAD
   # Current changes (from the branch you're merging into)
   =======
   # Incoming changes (from the branch you're merging)
   >>>>>>> feature/some-branch
   ```

4. **Resolution Steps**
   a. Open the conflicted file
   b. Look for conflict markers (<<<<<<, =======, >>>>>>>)
   c. Decide what code to keep:
      - Keep one version
      - Combine both versions
      - Write completely new code
   d. Remove conflict markers
   e. Test the merged code
   f. Commit the resolution

5. **In Our Case**
   - We combined both features:
     * Kept the input validation logic
     * Added the power operation
     * Updated validation to include the new operation
     * Tested to ensure both features work together

## Best Practices

1. **Before Resolving**
   - Understand both changes
   - Consult with team members if needed
   - Consider the impact on other parts of the code

2. **During Resolution**
   - Take time to understand the conflict
   - Don't rush the resolution
   - Test thoroughly after resolving

3. **After Resolution**
   - Review the final code
   - Run tests if available
   - Document significant decisions

## Common Git Commands for Merge Conflicts

```bash
# Check status of conflicted files
git status

# After resolving conflicts
git add <resolved-file>
git commit -m "Resolved merge conflict: description"

# If you need to abort the merge
git merge --abort

# To preview changes from both branches
git diff
```

Remember: Merge conflicts are normal in collaborative development. The key is to understand why they happen and handle them carefully to maintain code quality.