import streamlit as st

# title
st.title("This Is A Simple Calculater Made By Gokul❤️ ")

#taking inputs
string=st.text_input("PLEASE ENTER YOUR NAME (OPTIONAL)").upper()
num1=(st.number_input("ENTER FIRST NUMBER"))
num2=(st.number_input("ENTER SECOND NUMBER"))

#CHOOSE OPERATION

operation=st.selectbox("CHOOSE OPERATION",["ADDITION","SUBSTRACTION","MULTIPLLICATION","DIVISION"])

#OPERATION DONE
if st.button("CALCULATE"):
    if operation=="ADDITION":
        result=num1+num2
        st.balloons()
        st.success(f"YOUR RESULT IS {result}")
        if string:
         st.success(f"THANKYOU {string} 😊 FOR USING GOKUL'S CALCULATER")

    elif operation== "SUBSTRACTION":
        result=num1-num2
        st.balloons()
        st.success(f"YOUR RESULT IS{result}")
        if string:
         st.success(f"THANKYOU {string} 😊 FOR USING GOKUL'S CALCULATER")


    elif operation=="MULTIPLICATION":
        result=num1*num2
        st.balloons()
        st.success(f"YOUR RESLUT IS {result}")
        if string:
         st.success(f"THANKYOU {string} 😊 FOR USING GOKUL'S CALCULATER")

    else:
        operation=="DIVISION"
        if num2==0:
            st.error("CANNONT DEVIDE BY ZERO")
        else:
         result=num1/num2
         st.balloons()
         st.success(f"YOUR RESULT IS {result}")
         if string:
          st.success(f"THANKYOU {string} 😊 FOR USING GOKUL'S CALCULATER")
          