import streamlit as st

# title
st.title("Simple Calculator")

#taking inputs
stringg=st.text_input("PLEASE ENTER YOUR NAME (OPTIONAL)").upper()
num1=(st.number_input("ENTER FIRST NUMBER",step=1.0))
num2=(st.number_input("ENTER SECOND NUMBER",step=1.0))

#CHOOSE OPERATION

operation=st.selectbox("CHOOSE OPERATION",["ADDITION","SUBSTRACTION","Multiplication","DIVISION"])

#OPERATION DONE
if st.button("CALCULATE"):
    if operation=="ADDITION":
        result=num1+num2
        st.balloons()
        st.success(f"YOUR RESULT IS {result}")
        if stringg:
         st.success(f"THANKYOU {stringg} 😊 FOR USING GOKUL'S CALCULATER")
        else:
            stringg=="bablu","raj","gokul"
            print("O you are friend of Gokul")
          

    elif operation== "SUBSTRACTION":
        result=num1-num2
        st.balloons()
        st.success(f"YOUR RESULT IS{result}")
        if stringg:
         st.success(f"THANKYOU {stringg} 😊 FOR USING GOKUL'S CALCULATER")
        else:
            stringg=="bablu","raj","gokul"
            print("O you are friend of Gokul")
          

    elif operation=="Multiplication":
        result=num1 * num2
        st.balloons()
        st.success(f"YOUR RESULT IS {result}")
        if stringg:
         st.success(f"THANKYOU {stringg} 😊 FOR USING GOKUL'S CALCULATER")
        else:
            stringg=="bablu","raj","gokul"
            print("O you are friend of Gokul")
          

    else:
        operation=="DIVISION"
        if num2==0:
            st.error("CANNONT DEVIDE BY ZERO")
        else:
         result=num1/num2
         st.balloons()
         st.success(f"YOUR RESULT IS {result}")
         if stringg:
          st.success(f"THANKYOU {stringg} 😊 FOR USING GOKUL'S CALCULATER")
         else:
            stringg=="bablu","raj","gokul"
            print("O you are friend of Gokul")
          