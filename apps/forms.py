class FormMixin(object):
    def get_errors(self,):
        if hasattr(self,'errors'):
            errors=self.errors.get_json_data()
            new_errors={}
            for key,message_dicts in errors.items():
                messages=[]
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key]=message
            return new_errors
        else:
            return {}

        #get_errors返回的数据格式{'password':['密码最大长度不超过20个字符','xxx'],'telephone':['xxx','xx']}