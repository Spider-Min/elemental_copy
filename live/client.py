import requests
from jinja2 import Template


class ElementalLive():
    def __init__(self, server_ip):
        self.server_ip = server_ip


    # Simple version of generate_header, may need more paras in the future(like api_key)
    def generate_headers(self):
        return {
            'Accept': 'application/xml',
            'Content-Type': 'application/xml'
        }


    # Create event, options contain username, password and mediastore_container url
    def create_event(self, template_path, options):

        # Initiate url
        url = f'{self.server_ip}/live_events'

        # Generate template
        xml_file = open(template_path, 'r')
        xml_content = xml_file.read()
        template = Template(xml_content)

        # Pass params to template
        body = template.render(**options)

        # Send request
        response = requests.request(method='POST', url=url, data=body,
                                    headers=self.generate_headers())

        return response

    def delete_event(self, event_id):

        #Initial url
        url = f'{self.server_ip}/live_events/{event_id}'

        # Send request
        response = requests.request(method='DELETE', url=url)

        return response

    def start_event(self, event_id):

        #Initail url
        url = f'{self.server_ip}/live_events/{event_id}/start'

        # Generate body
        body = "<start></start>"

        #Send request
        response = requests.request(method='POST', url=url, data=body,
                                    headers=self.generate_headers())

        return response

    def stop_event(self, event_id):

        #Initail url
        url = f'{self.server_ip}/live_events/{event_id}/stop'

        # Generate body
        body = "<stop></stop>"

        #Send request
        response = requests.request(method='POST', url=url, data=body,
                                    headers=self.generate_headers())

        return response


