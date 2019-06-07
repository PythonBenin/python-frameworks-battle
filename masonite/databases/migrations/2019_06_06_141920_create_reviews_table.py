from orator.migrations import Migration


class CreateReviewsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('reviews') as table:
            table.increments('id')
            table.string('company')
            table.string('job')
            table.string('headline')
            table.text('pros')
            table.text('cons')
            table.integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('reviews')
