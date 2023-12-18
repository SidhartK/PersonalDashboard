import streamlit as st
import pandas as pd 
from db_fxns import * 
import streamlit.components.v1 as stc
from streamlit_datalist import stDatalist



# Data Viz Pkgs
import plotly.express as px 


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">ToDo App (CRUD)</h1>
    <p style="color:white;text-align:center;">Built with Streamlit</p>
    </div>
    """


def app():
	stc.html(HTML_BANNER)


	menu = ["Create","Read","Update","Delete","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	create_table()

	if choice == "Create":
		st.subheader("Add Item")
		col1,col2 = st.columns(2)
		
		with col1:
			name = st.text_input("Task Name")
			area = stDatalist("This datalist is...", ["great", "cool", "neat"])
			description = st.text_area("Task Description")

		with col2:
			priority = st.selectbox("Priority",Task.OPTIONS["priority"])
			status = Task.OPTIONS["status"][1] if st.toggle("Task Done") else Task.OPTIONS["status"][0]
			due_date = st.date_input("Due Date")
			due_time = st.time_input("Time", datetime.time(0, 0), step=datetime.timedelta(minutes=5))
			due_at = datetime.datetime.combine(due_date,due_time)
		
		if st.button("Add Task"):
			import pdb; pdb.set_trace()
			task = Task(
				name=name,
				status=status,
				area=area,
				priority=priority,
				due_at=due_at,
				description=description
			)
			add_data(Task(name=task,status=task_status,due_date=task_due_date))
			st.success("Added ::{} ::To Task List".format(name))


	elif choice == "Read":
		# st.subheader("View Items")
		with st.expander("View All"):
			result = view_all_data()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
			st.dataframe(clean_df)

		with st.expander("Task Status"):
			task_df = clean_df['Status'].value_counts().to_frame()
			# st.dataframe(task_df)
			task_df = task_df.reset_index()
			st.dataframe(task_df)
			p1 = px.pie(task_df,names='Status',values='count', title='Task Status')
			st.plotly_chart(p1,use_container_width=True)


	elif choice == "Update":
		st.subheader("Edit Items")
		with st.expander("Current Data"):
			result = view_all_data()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=Task.get_key_list())
			st.dataframe(clean_df)

		import pdb; pdb.set_trace()
		# list_of_tasks = [i[0] for i in view_all_task_names()]
		# selected_task = st.selectbox("Task",list_of_tasks)
		# task_result = get_task(selected_task)
		# st.write(task_result)

		if task_result:
			task = task_result[0][0]
			task_status = task_result[0][1]
			task_due_date = task_result[0][2]

			col1,col2 = st.columns(2)
			
			with col1:
				new_task = st.text_area("Task To Do",task)

			with col2:
				new_task_status = st.selectbox(task_status,["ToDo","Doing","Done"])
				new_task_due_date = st.date_input(task_due_date)

			if st.button("Update Task"):
				edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
				st.success("Updated ::{} ::To {}".format(task,new_task))

			with st.expander("View Updated Data"):
				result = view_all_data()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_task_names()]
		delete_by_task_name =  st.selectbox("Select Task",unique_list)
		if st.button("Delete"):
			delete_data(delete_by_task_name)
			st.warning("Deleted: '{}'".format(delete_by_task_name))

		with st.expander("Updated Data"):
			result = view_all_data()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
			st.dataframe(clean_df)

	else:
		st.subheader("About ToDo List App")
		st.info("Built with Streamlit")
		st.info("Jesus Saves @JCharisTech")
		st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
	app()

