# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ofsc', 'ofsc.tests']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.1.2,<8.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'ofsc',
    'version': '1.16.5',
    'description': 'Python wrapper for Oracle Field Service API',
    'long_description': '## OFSC\n\nA simple Python wrapper for Oracle OFS REST API\n\n## Functions implemented\n\n\n### Core / Activities\n    get_activities (self, params, response_type=TEXT_RESPONSE)\n    get_activity (self, activity_id, response_type=TEXT_RESPONSE):\n    update_activity (self, activity_id, data, response_type=TEXT_RESPONSE)\n    move_activity (self, activity_id, data, response_type=TEXT_RESPONSE)\n    get_file_property(self, activityId, label, mediaType="application/octet-stream", response_type=FULL_RESPONSE)\n    get_all_activities( self, root, date_from, date_to, activity_fields, initial_offset=0, limit=5000)\n    search_activities(self, params, response_type=TEXT_RESPONSE)\n\n\n### Core / Events\n    get_subscriptions(self, response_type=TEXT_RESPONSE)\n    create_subscription(self, data, response_type=TEXT_RESPONSE)\n    delete_subscription(self, subscription_id, response_type=FULL_RESPONSE)\n    get_subscription_details(self, subscription_id, response_type=TEXT_RESPONSE)\n    get_events(self, params, response_type=TEXT_RESPONSE)\n\n### Core / Resources\n    create_resource(self, resourceId, data, response_type=TEXT_RESPONSE)\n    get_resource(self, resource_id, inventories=False, workSkills=False, workZones=False, workSchedules=False , response_type=TEXT_RESPONSE)\n    get_position_history(self, resource_id,date,response_type=TEXT_RESPONSE)\n    get_resource_route(self, resource_id, date, activityFields = None, offset=0, limit=100, response_type=TEXT_RESPONSE)\n    get_resource_descendants(self, resource_id,  resourceFields=None, offset=0, limit=100, inventories=False, workSkills=False, workZones=False, workSchedules=False, response_type=TEXT_RESPONSE)\n\n### Core / Users\n    get_users(self, offset=0, limit=100, response_type=FULL_RESPONSE)\n    get_user(self, login, response_type=FULL_RESPONSE):\n    update_user (self, login, data, response_type=TEXT_RESPONSE)\n    create_user(self, login, data, response_type=FULL_RESPONSE)\n    delete_user(self, login, response_type=FULL_RESPONSE)\n\n### Daily Extract\n    get_daily_extract_dates(self, response_type=FULL_RESPONSE)\n    get_daily_extract_files(self, date, response_type=FULL_RESPONSE)\n    get_daily_extract_file(self, date, filename, response_type=FULL_RESPONSE)\n\n### Metadata / Capacity\n    get_capacity_areas (self, expand="parent", fields=capacityAreasFields, status="active", queryType="area", response_type=FULL_RESPONSE)\n    get_capacity_area (self,label, response_type=FULL_RESPONSE)\n\n### Metadata / Activity Types\n    get_activity_type_groups (self, expand="parent", offset=0, limit=100, response_type=FULL_RESPONSE)\n    get_activity_type_group (self,label, response_type=FULL_RESPONSE)   \n    get_activity_types(self, offset=0, limit=100, response_type=FULL_RESPONSE)\n    get_activity_type (self, label, response_type=FULL_RESPONSE)\n\n### Metadata / properties\n    get_properties (self, offset=0, limit=100, response_type=FULL_RESPONSE)\n     get_all_properties(self, initial_offset=0, limit=100)\n\n## Test History\n\nOFS REST API Version | PyOFSC\n------------ | -------------\n20C| 1.7\n21A| 1.8, 1.8,1, 1.9\n21D| 1.15\n22B| 1.16\n\n',
    'author': 'Borja Toron',
    'author_email': 'borja.toron@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/btoron/pyOFSC',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
