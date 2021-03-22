# put your DB router classes here...

# class MyDBRouter:
#     """
#     Route queries to specified database
#     """
#     def db_for_read(self, model, **hints):
#         if model._meta.label.split('.')[-1] == 'modelname':
#             pass  # logic for particular model
#         # logic to select which database
#         return "db alias"
#
#     def db_for_write(self, model, **hints):
#         # logic to select which database
#         return "db alias"
#
#     def allow_relation(self, obj1, obj2, **hints):
#         pass
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         pass
