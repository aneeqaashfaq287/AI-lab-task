class BookRequest:
    def __init__(self, studentName, bookName, priority):
        self.studentName = studentName
        self.bookName = bookName
        self.priority = priority
        self.next = None


class LibraryPriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def Add(self, request):

        if self.front is None:
            self.front = request
            self.rear = request
            return

        if request.priority < self.front.priority:
            request.next = self.front
            self.front = request
            return

        current = self.front

        while (current.next is not None and
               current.next.priority <= request.priority):
            current = current.next

        request.next = current.next
        current.next = request

        if request.next is None:
            self.rear = request

    def Remove(self):

        if self.front is None:
            return None

        request = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        request.next = None

        return request

    def IsEmpty(self):
        return self.front is None

    def Display(self):

        if self.IsEmpty():
            print("No pending book requests.")
            return

        current = self.front

        print("\n===== Book Requests =====")

        while current is not None:
            print("Student:", current.studentName)
            print("Book:", current.bookName)
            print("Priority:", current.priority)
            print("------------------------")

            current = current.next


queue = LibraryPriorityQueue()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book Request")
    print("2. Process Request")
    print("3. Display Requests")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        studentName = input("Enter Student Name: ")
        bookName = input("Enter Book Name: ")
        priority = int(input("Enter Priority (1-3): "))

        if priority < 1 or priority > 3:
            print("Invalid priority.")
        else:
            request = BookRequest(
                studentName,
                bookName,
                priority
            )

            queue.Add(request)

            print("Request added successfully.")

    elif choice == "2":

        request = queue.Remove()

        if request is None:
            print("No requests available.")
        else:
            print("\n===== Processing Request =====")
            print("Student:", request.studentName)
            print("Book:", request.bookName)
            print("Priority:", request.priority)

    elif choice == "3":

        queue.Display()

    elif choice == "4":

        print("Program terminated.")
        break

    else:
        print("Invalid choice.")