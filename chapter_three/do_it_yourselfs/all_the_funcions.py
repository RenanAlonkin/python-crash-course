# 3.10 Use all the functions on this chapter

tasks = []

tasks.append("1 - cleaning my room")
tasks.insert(1, "3 - buying a new ___")
tasks.append("2 - study python")

print(tasks)

# We need to sort the tasks
tasks.sort()
print(tasks)

# Oh no, the last task has a problem, we need to
# Overwrite it

tasks[-1] = "3 - buying a new notebook"

# Now our list is okay, let's check how many tasks do we have
len(tasks)

# Lets see it in reverse
print(sorted(tasks, reverse=True))

# Okay, now let's do the tasks

first_task_done = tasks.pop()
print(first_task_done)

second_task_done = tasks.pop()
print(second_task_done)

third_task_done = tasks.pop()
print(third_task_done)

# Now let's see if there is anything else to do
print(tasks)
