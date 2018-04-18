from django_app_lti.views import LTILaunchView

class MyLTILaunchView(LTILaunchView):
    def hook_before_post(self, request):
        '''Called before models are created and initialized in hook_process_post().'''
        print self.request
        pass

    def hook_process_post(self, request):
        '''Creates and initializes models.'''
        super(MyLTILaunchView, self).hook_process_post(request)

    def hook_after_post(self, request):
        '''Called after models are initialized.'''
        pass

    def hook_get_redirect(self):
        '''Returns a redirect after the POST request has been processed.'''
        return super(MyLTILaunchView, self).hook_get_redirect()