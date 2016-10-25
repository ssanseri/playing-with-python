epic_programmer_dict = {'Tim Berners-Lee' : 'tbl@gmail.com',
                        'Guido van Rossum' : 'gvr@gmail.com',
                        'Linus Torvalds': 'lt@gmail.com',
                        }

# Add Larry Page and his email to the dictionary
epic_programmer_dict['Larry Page'] = 'lp@gmail.com'
epic_programmer_dict['Sergey Brin'] = 'sb@gmail.com'
epic_programmer_dict['Me'] = 'me@gmail.com'

# Delete Sergey Brin from the dictionary
if 'Sergey Brin' in epic_programmer_dict:
    del epic_progammer_dict['Sergey Brin']

print (epic_programmer_dict)
