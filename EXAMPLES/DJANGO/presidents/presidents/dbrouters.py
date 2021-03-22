

class PresidentRouter:
    """
    Route president queries to the 'potus' database
    """
    def db_for_read(self, model, **hints):
        """
        Called for read operations on all databases

        :param model: model being queried
        :param hints: dict of hints; only key is "instance"
        :return: DB alias or None
        """
        if model._meta.label.split('.')[-1] == 'Presidents':
            return 'potus'

    # def db_for_write(self, model, **hints):
    #     pass
    #
    # def allow_relation(self, obj1, obj2, **hints):
    #     pass
    #
    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     pass
