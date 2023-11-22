<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Siddhant Nayak (Sid) (sgn26)</td></tr>
<tr><td> <em>Generated: </em> 4/24/2023 11:16:00 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/sgn26" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233859383-a760787a-f79c-4c6f-bc6c-fe65042341a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233858932-c9e39af7-33d4-4220-93c4-7fa7f2faf3c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233858926-fa9502a2-6f6d-4c84-ab89-d8da3a1d5d87.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233858928-b369844c-d5ba-47b1-ae72-37bb30fc915c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation (already registered)<br></p>
</td></tr>
<tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233858931-22709254-4124-47a4-b4c4-da7effcab2c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233858929-924dc85b-de8c-47fc-8290-c7b3ffcaaf86.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successfully registered <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233859304-89d91f87-5cef-401f-96a1-356d7f4a8089.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data from the sql table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Sid216/IS601-006/pull/22">https://github.com/Sid216/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>To register, it gets data from the user and inserts it into the<br>users table based on the appropriate column. If an email or username is<br>taken it checks the duplicate and flashes a message. If everything is fine<br>then it successfully registers the user.<br class="Apple-interchange-newline">validate_on_submit is used from wtf.forms to make<br>sure entered data matches with the data in db<div>For password bcrypt is used<br>to hash out the contents within the password.</div><div>DB is used insert the changes<br>into the specified column and data is stored for later to be called<br>for login.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233859697-09480f22-fe23-4c0b-b470-6c97720b53e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch validation (doesn&#39;t match what&#39;s in the DB)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234025048-177b6a11-4e63-48da-ab8a-10c36e8a61b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234023562-569deb6f-b229-4c9e-8178-6ac170f8fd6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash message and/or a redirect to a landing page (post-login)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Sid216/IS601-006/pull/22">https://github.com/Sid216/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>DB is utilized to compare the entered data to the data in db<br>to make sure the entered email/password combo is correct or not.<div>bcrypt is used<br>to hash the password entered.&nbsp;</div><div>validate_on_submit is used from wtf.forms to make sure entered<br>data matches with the data in db</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234024279-efa37c59-9416-43de-bdc1-86d20eb7a727.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing something about being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Sid216/IS601-006/pull/22">https://github.com/Sid216/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Remove session keys set by Flask-Principal in turn logs user off.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234085350-69c499a4-9773-4868-90b5-635cceae7755.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When i try to access the roles page with <a href="mailto:&#x73;&#105;&#x64;&#x40;&#100;&#x75;&#x6d;&#121;&#46;&#99;&#111;&#x6d;">&#x73;&#105;&#x64;&#x40;&#100;&#x75;&#x6d;&#121;&#46;&#99;&#111;&#x6d;</a> it gives an<br>appropriate error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234083933-45ce03b9-9790-40d3-ad7a-d2e8d8b74372.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin role<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234084155-81ddec54-9588-4ca3-ae2e-6597c27f9c5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New admin created SidTheAdmin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234084617-5e9e9457-8b79-4829-9b0e-23a07ce4038b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is my admin user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Sid216/IS601-006/pull/22">https://github.com/Sid216/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>any user who has registered can access the profile page. If a user<br>who has no account registered tries to access the page it doesnt allow<br>that user to view the details.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>to assign role one has to be an admin. Its the same way<br>that I cannot give myself 10/10 for the final project because my role<br>is of a student. If my role was a TA I would be<br>able to do that.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234072222-c9bf8427-b527-409c-9082-f2956f2eb8e8.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234072225-f7bf6cb1-291a-4ee6-a42f-857f51418357.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234072227-6ed3b0b0-14ac-4220-b508-d9f6901906f9.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Sid216/IS601-006/pull/22">https://github.com/Sid216/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>I just did&nbsp;<span style="background-color: rgb(0, 0, 0); white-space: pre; font-size: 12px; font-family: Menlo,<br>Monaco, &quot;Courier New&quot;, monospace; color: rgb(212, 212, 212);">font-family</span><span style="background-color: rgb(0, 0, 0); white-space:<br>pre; font-size: 12px; font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace;">: </span><span style="background-color: rgb(0, 0,<br>0); white-space: pre; font-size: 12px; font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; color: rgb(206,<br>145, 120);">Georgia</span><span style="background-color: rgb(0, 0, 0); white-space: pre; font-size: 12px; font-family: Menlo, Monaco,<br>&quot;Courier New&quot;, monospace;">, </span><span style="background-color: rgb(0, 0, 0); white-space: pre; font-size: 12px; font-family:<br>Menlo, Monaco, &quot;Courier New&quot;, monospace; color: rgb(206, 145, 120);">&#39;Times New Roman&#39;</span><span style="background-color: rgb(0,<br>0, 0); white-space: pre; font-size: 12px; font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace;">, </span>&lt;span<br>style=&quot;background-color: rgb(0, 0, 0); white-space: pre; font-size: 12px; font-family: Menlo, Monaco, &quot;Courier New&quot;,<br>monospace; color: rgb(206, 145, 120);&quot;&gt;Times</span><span style="background-color: rgb(0, 0, 0); white-space: pre; font-size: 12px;<br>font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace;">, </span><span style="background-color: rgb(0, 0, 0); white-space: pre;<br>font-size: 12px; font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace; color: rgb(206, 145, 120);">serif</span><span style="background-color:<br>rgb(0, 0, 0); white-space: pre; font-size: 12px; font-family: Menlo, Monaco, &quot;Courier New&quot;, monospace;">;<br></span>wherever it was appropriate <div style="background-color: rgb(0, 0, 0); font-family: Menlo, Monaco, &quot;Courier<br>New&quot;, monospace; font-size: 12px; line-height: 18px; white-space: pre;"><div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234044002-4428b92f-9027-43b6-9161-23a043c3ee9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>chosen email is already taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234025048-177b6a11-4e63-48da-ab8a-10c36e8a61b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid user message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/233858926-fa9502a2-6f6d-4c84-ab89-d8da3a1d5d87.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mush match message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Sid216/IS601-006/pull/22">https://github.com/Sid216/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>Just typing it out like a normal print statement?<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234036117-306ad3d6-257d-4251-8ab0-32df7a4a5293.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username prefilled properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Sid216/IS601-006/pull/22">https://github.com/Sid216/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>based on the login email or username, its been pulled from the DB<br>using form inheritance<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234036982-afb2beea-2557-42ec-b856-43e74e6034e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234037225-be82f1a1-253a-45a5-8786-3e2fe2ffbcd7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234042744-b547f94b-c0f8-4fb8-80fa-c20a3d6142e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email and username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234044002-4428b92f-9027-43b6-9161-23a043c3ee9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email/username already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234042202-ba066dd0-582f-47d2-9a80-679556ed0af7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before updating<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/57045571/234043068-17bd4ee6-deee-4365-8a51-05be4c885d19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After updating<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Sid216/IS601-006/pull/22">https://github.com/Sid216/IS601-006/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>It gets data from user using form.---.data. It then selects the data using<br>DB.selectOne and compares the two. If a chnge is seen then it uses<br>DB.update to update that field and flashes a message if it was successful<br>or not.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sgn26-prod.herokuapp.com/">https://is601-sgn26-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/sgn26" target="_blank">Grading</a></td></tr></table>