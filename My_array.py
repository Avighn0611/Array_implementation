class PriorityQueueArray:
    def __init__(self):
        """
        Initialize the priority queue as an array.
        """
        self.queue = []

    def insert(self, patient):
        """
        Add a new patient to the queue, maintaining priority order.
        """
        if patient.esi_priority is None:
            print(f"Patient {patient.name} does not have an assigned priority. Please calculate priority first.")
            return

        # Insert the patient while maintaining the order based on priority
        self.queue.append(patient)
        self.queue.sort(key=lambda p: (p.esi_priority, p.arrival_time))
        print(f"Patient {patient.name} with priority {patient.esi_priority} added to the queue.")

    def extract_max(self):
        """
        Remove and return the patient with the highest priority (lowest ESI value).
        """
        if not self.queue:
            print("No patients in the queue.")
            return None

        # Pop the first patient as it's the highest priority due to sorting
        return self.queue.pop(0)

    def __bool__(self):
        """
        Check if the queue is not empty.
        """
        return len(self.queue) > 0

    def list_all(self):
        """
        Return all patients in the queue in priority order.
        """
        return self.queue


# Example Usage
# Replace the BinomialHeap class in PatientManager with PriorityQueueArray.
