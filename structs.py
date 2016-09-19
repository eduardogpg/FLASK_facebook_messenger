def text_message(recipient_id, message_text):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': { 'text': message_text}
    }
    return message_data

def typing_message(recipient_id):
    message_data = {
        'recipient': {'id': recipient_id},
        'sender_action' : 'typing_on'
    }
    return message_data

def item_quick_replies(title, payload):
    data =  {
				"content_type":"text",
				"title": title,
				"payload": payload
		}
    return data

def quick_replies(recipient_id, text, quick_replies = [] ):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': {    
            'text': text,
            'quick_replies': quick_replies
        }
    }
    return message_data
