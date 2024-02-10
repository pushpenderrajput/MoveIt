import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st
def send_email(name, phone, from_address, to_address, date, items):
    msg = MIMEMultipart()
    msg['From'] = 'pushpenderrajputsp@gmail.com'
    msg['To'] = 'pushpenderrajputsp@gmail.com'
    msg['Subject'] = 'New form submission'

    body = f'Name: {name}\n' \
           f'Phone: {phone}\n' \
           f'From: {from_address}\n' \
           f'To: {to_address}\n' \
           f'Date: {date}\n' \
           f'Items: {items}'

    msg.attach(MIMEText(body, 'plain'))

def send_email_smtp(msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('pushpenderrajputsp@gmail.com', 'Pushpender@21')
        text = msg.as_string()
        server.sendmail('pushpenderrajputsp@gmail.com', 'pushpenderrajputsp@gmail.com', text)
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print('Error sending email:', e)



if __name__ == '__main__':
    st.title('Contact Form')

    name = st.text_input('Your Name')
    phone = st.text_input('Your contact number')
    from_address = st.text_input('Move from')
    to_address = st.text_input('Move to')
    date = st.date_input('Shifting Date')
    items = st.text_area('Major Item list', 'Enter items here')

    if st.button('Submit'):
        if name and phone and from_address and to_address and date and items:
            send_email(name, phone, from_address, to_address, date.strftime('%Y-%m-%d'), items)
            st.success('Email sent successfully.')
        else:
            st.warning('Please fill in all the fields.')