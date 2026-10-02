class Service:
 def run(self,value): return {'task':value,'plan':['inspect repository','identify files','propose patch','run tests','human review'],'approval_required':True}