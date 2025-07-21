#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    try:
        if type(template) is not str:
            raise TypeError('template argument must be a string.')
        if not all(isinstance(row, dict) for row in attendees):
            raise ValueError('attendees argument must be a list of dicts.')
        if len(template) == 0:
            raise ValueError('Template is empty, no output files generated.')
        if len(attendees) == 0:
            raise ValueError('No data provided, no output files generated.')

        for i, attendee in enumerate(attendees, start=1):
            new_template = template;
            for tag in ['name', 'event_title', 'event_date', 'event_location']:
                value = attendee.get(tag)
                if not value:
                    value = 'N/A'
                new_template = new_template.replace(f'{{{tag}}}', str(value))

            filename = f'output_{i}.txt'

            if os.path.exists(filename):
                raise FileExistsError(f'{filename} already exists.')

            with open(filename, 'w') as file:
                file.write(new_template)

    except Exception as err:
        print(err)
