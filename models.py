from mongoengine import Document, fields
from datetime import datetime

class Entry(Document):
    user_id = fields.IntField(required=True)  # Store Django User ID
    username = fields.StringField(required=True)  # Store username for easier queries
    salary = fields.DecimalField(max_digits=10, decimal_places=2, required=True)
    budget = fields.DecimalField(max_digits=10, decimal_places=2, required=True)
    expenses = fields.DecimalField(max_digits=10, decimal_places=2, required=True)
    date = fields.DateTimeField(default=datetime.now)

    meta = {
        'collection': 'entries',
        'ordering': ['-date']
    }

    def __str__(self):
        return f"{self.username} - {self.date.strftime('%Y-%m-%d')}"

class DetailedEntry(Document):
    user_id = fields.IntField(required=True)  # Store Django User ID
    username = fields.StringField(required=True)  # Store username for easier queries
    salary = fields.DecimalField(max_digits=10, decimal_places=2, required=True)
    date = fields.DateTimeField(default=datetime.now)

    # Budget categories
    budget_education = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget_entertainment = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget_housing = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget_transport = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget_food = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget_utilities = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget_others = fields.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Expense categories
    expense_education = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense_entertainment = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense_housing = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense_transport = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense_food = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense_utilities = fields.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense_others = fields.DecimalField(max_digits=10, decimal_places=2, default=0)

    meta = {
        'collection': 'detailed_entries',
        'ordering': ['-date']
    }

    @property
    def total_budget(self):
        return (self.budget_education + self.budget_entertainment + self.budget_housing +
                self.budget_transport + self.budget_food + self.budget_utilities + self.budget_others)

    @property
    def total_expenses(self):
        return (self.expense_education + self.expense_entertainment + self.expense_housing +
                self.expense_transport + self.expense_food + self.expense_utilities + self.expense_others)

    def __str__(self):
        return f"{self.username} - Detailed Entry - {self.date.strftime('%Y-%m-%d')}"
