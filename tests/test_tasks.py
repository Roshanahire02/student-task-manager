from tasks import add_task


def test_add_task():
    add_task("Test task")

    with open("data/tasks.txt", "r") as file:
        content = file.read()

    assert "Test task" in content