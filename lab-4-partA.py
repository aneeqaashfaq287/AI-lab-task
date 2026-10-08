class BookRequestNode:
    def __init__(self, studentID, studentName, bookID, bookTitle, priority):
        self.studentID = studentID
        self.studentName = studentName
        self.bookID = bookID
        self.bookTitle = bookTitle
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def Add(self, request):
        request.next = None

        if self.front is None:
            self.front = request
            self.rear = request

        elif request.priority < self.front.priority:
            request.next = self.front
            self.front = request

        else:
            current = self.front

            while (current.next is not None and
                   current.next.priority <= request.priority):
                current = current.next

            request.next = current.next
            current.next = request

            if request.next is None:
                self.rear = request

        self.count += 1

    def Remove(self):
        if self.front is None:
            return None

        request = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        request.next = None
        self.count -= 1

        return request

    def IsEmpty(self):
        return self.front is None

    def IsNotEmpty(self):
        return self.front is not None

    def PrintQueue(self):
        if self.IsEmpty():
            print("Queue is empty.")
            return

        current = self.front

        while current is not None:
            print("-----------------------------")
            print("Student ID:", current.studentID)
            print("Student Name:", current.studentName)
            print("Book ID:", current.bookID)
            print("Book Title:", current.bookTitle)
            print("Priority:", current.priority)

            current = current.next

        print("-----------------------------")


queue = PriorityQueue()

while True:

    print("\n===== Library Book Request System =====")
    print("1. Add Book Request")
    print("2. Process Highest Priority Request")
    print("3. Display All Requests")
    print("4. Check Queue Status")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        studentID = int(input("Enter Student ID: "))
        studentName = input("Enter Student Name: ")
        bookID = int(input("Enter Book ID: "))
        bookTitle = input("Enter Book Title: ")
        priority = int(input("Enter Priority (1-3): "))

        if priority < 1 or priority > 3:
            print("Invalid priority.")
        else:
            request = BookRequestNode(
                studentID,
                studentName,
                bookID,
                bookTitle,
                priority
            )

            queue.Add(request)
            print("Book request added successfully.")

    elif choice == "2":

        request = queue.Remove()

        if request is None:
            print("Queue is empty.")
        else:
            print("\n===== Processing Request =====")
            print("Student ID:", request.studentID)
            print("Student Name:", request.studentName)
            print("Book ID:", request.bookID)
            print("Book Title:", request.bookTitle)
            print("Priority:", request.priority)

    elif choice == "3":

        print("\n===== All Requests =====")
        queue.PrintQueue()

    elif choice == "4":

        if queue.IsEmpty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")
            print("Total requests:", queue.count)

    elif choice == "5":

        print("Program terminated.")
        break

    else:
        print("Invalid choice.")