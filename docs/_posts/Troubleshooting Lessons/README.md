# Troubleshooting Instructions

<img src="../images/Data Science Thumbnail.png">

<!DOCTYPE html>
<html><body><h1>TROUBLESHOOTING LESSONS (Copy of LP)</h1><br><h2>Table of Contents:</h2><ol>1. Kernel Error / Jupyter Missing "Python (dojo-env)" in kernels<br>2. conda activate error - GitBash<br>3. "code" Command Not Working (Mac)<br>4. GitBash Error: Could Not Fork Child Process<br>5. Installing Graphviz (Windows)<br>6. Reinstalling Dojo-Env<br>7. Uninstalling Anaconda (Completely)<br>8. GitBash Opens in the Wrong Folder<br></ol><br><hr></hr><br><h1>1. Kernel Error / Jupyter Missing "Python (dojo-env)" in kernels</h1>
<h2>PROBLEM:</h2>
<p></p>
<ul>
	<li><strong>If you see a message like this when trying to open the environment testing notebook:<br></strong></li>
</ul>
<figure><img
		src="../images/lp/kernel_error.png">
</figure>
<p></p>
<ul>
	<li><strong>OR if "Python (dojo-env)" doesn't show up in Jupyter Notebook in EITHER:</strong>
		<ul>
			<li>The "New" menu on the Files tab in Jupyter.</li>
		</ul>
	</li>
	<li>
		<figure><img
				src="../images/lp/missing_kernel_new.png"
				style="width: 620px; height: 277px;" width="620" height="277"><br></figure>
		<ul>
			<li>
				<p>or the Kernel &gt; Change Kernel menu inside a Jupyter Notebook:<br></p>
				<figure><img
						src="../images/lp/missing_kernel_notebook.png"
						style="width: 519px; height: 323px;" width="519" height="323"><span></span></figure>
			</li>
		</ul>
	</li>
</ul>
<h2>Solution</h2>
<ul>
	<li>You missed a command after running the conda env create command during step 2, so let's rerun the command.</li>
	<li>First, shut down Jupyter Notebook <ul>
			<li>The quickest way is to go back to the Terminal/GitBash window that you used to start the notebook and
				press "control + C"</li>
		</ul>
	</li>
</ul>
<ul>
	<li><strong>In your terminal/GitBash, make sure it says (dojo-env) above or next to your terminal prompt.</strong>
		<ul>
			<li>if not, on Mac run: <ul>
					<li>"conda activate dojo-env"</li>
				</ul>
			</li>
			<li>on Windows run:<ul>
					<li>"source activate dojo-env"</li>
				</ul>
			</li>
		</ul>
	</li>
	<li><strong>Then run the command below to install dojo-env as a kernel in jupyter:</strong></li>
</ul>
<pre>python -m ipykernel install --user --name dojo-env --display-name "Python (dojo-env)"</pre>
<p>Then, go ahead and boot up jupyter notebook and try again. It should now know the "Python (dojo-env)" kernel.</p><br><hr></hr><br><h1>2. conda activate error - GitBash</h1>
<h2>PROBLEM:</h2>
<ul>
	<li>You see the following error message in GitBash:</li>
</ul>
<pre>CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run
    $ conda init &lt;shell_name&gt;
Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell
See 'conda init --help' for more information and options.&lt;/shell_name&gt;
</pre>
<h3>Solution 1:</h3>
<ul>
	<li>For your computer, run "source activate dojo-env" instead of conda activate.<ul>
			<li>ANYTIME you see a set of instructions that says to run "conda activate" you should ALWAYS replace the
				word "conda" with "source". </li>
		</ul>
	</li>
</ul>
<pre>source activate dojo-env</pre>
<div>
	<h3>PROBLEM - V2: </h3>
</div>
<div>
	<ul>
		<li>If you are seeing this message EVERY time you open a new GitBash Window. </li>
	</ul>
	<p>Solution 2: </p>
	<ul>
		<li>During step 2, you were told to run the following echo conda activate command but your computer requires you
			to use "source activate" instead of "conda activate"</li>
	</ul>
	<pre>## INCORRECT What you ran previously
echo "conda activate dojo-env" &gt;&gt; ~/.bash_profile</pre>
	<ul>
		<li><strong>Step 1) To fix this, you need to open the hidden file ".bash_profile" in VS Code to fix the
				command</strong>.<ul>
				<li>In GitBash run the following command to open the file in VS Code.</li>
			</ul>
		</li>
	</ul>
	<pre>code ~/.bash_profile</pre>
	<ul>
		<li><strong>If this doesn't work and says file not found,</strong> change the "~./" to your full file path to
			your user folder:<ul>
				<li>In the example below, replace &lt;USERFOLDER&gt; with your actual User account name.<p><br></p>
					<ul>
						<li>Note: if you do not know your username, run the "whoami" command in GitBash. The text
							displayed is your &lt;USERFOLDER&gt;</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
	<pre>code /c/Users/&lt;USERFOLDER&gt;/.bash_profile</pre>
	<p><br></p>
	<ul>
		<li><strong>Step 2) in the vs code window that opens, you should see the 3 lines of text below. <br></strong>
		</li>
	</ul>
	<pre>conda activate dojo-env
alias jnb="jupyter notebook"
alias lab="jupyter lab"</pre>
	<ul>
		<li>Replace the word "conda" with "source" and then click on File &gt; Save.</li>
		<ul>
			<li>So your final .bash_profile should now say: </li>
		</ul>
	</ul>
	<pre>source activate dojo-env
alias jnb="jupyter notebook"
alias lab="jupyter lab"</pre>
	<p> (Note: it is okay if there is additional text in this file. Whats important is that you change the conda
		activate command to source activate.) </p>
	<p><br></p>
	<ul>
		<li><strong>Step 3) Open a NEW GitBash window and the message should no longer appear!</strong></li>
	</ul>
</div><br><hr></hr><br><p><br></p>
<h1>3. "code" Command Not Working (Mac)</h1>
<p><br></p>
<figure><img
		src="../images/lp/code_not_found.png">
</figure>
<p><br></p>
<ul>
	<li>If you are trying to open VS Code using the "code" command in your Terminal and receive an error message that
		says </li>
</ul>
<pre>command not found: code</pre>
<ul>
	<li><strong>Open VS Code manually</strong> (check the Applications folder or use Spotlight Search)</li>
	<li>Open the Command Palette. <ul>
			<li>On the menu bar (top of the screen), select "View" &gt; and then select "Command Palette"</li>
		</ul>
	</li>
</ul>
<figure><img
		src="../images/lp/command_palette.png"
		style="width: 590px; height: 476px;" width="590" height="476"></figure>
<ul>
	<li>A popup window will appear with a "&gt;" prompt. </li>
</ul>
<figure><img
		src="../images/lp/command_palette_popup.png"
		style="width: 465px; height: 252px;" width="465" height="252"></figure>
<p><br></p>
<ul>
	<li>Start typing "install code" and you should see the option appear for "Shell Command: Install 'code' command in
		PATH". <ul>
			<li>Click on this option.</li>
		</ul>
	</li>
</ul>
<figure><img
		src="../images/lp/install_code_command.png"
		style="width: 568px; height: 84px;" width="568" height="84"></figure>
<ul>
	<li>It will then notify you that you will be prompted to give "osascript" administrative privileges.</li>
</ul>
<p><br></p>
<figure><img
		src="../images/lp/code_command_prompt.png"
		style="width: 246px; height: 214px;" width="246" height="214"></figure>
<p><br></p>
<ul>
	<li> Click OK and then on the next pop-up window, enter your normal password for your Mac.<ul>
			<li>You should see a success message like the one below. </li>
		</ul>
	</li>
</ul>
<figure><img
		src="../images/lp/success_code_command.png"
		style="width: 322px; height: 241px;" width="322" height="241"></figure>
<p></p>
<ul>
	<li>You are all set! Try the code command again.</li>
</ul>
<p><br></p>
<ul>
	<li><strong>NOTE: if you get an error message when running the install code command:</strong>
		<ul>
			<li>First UNinstall the code command (which is counter-intuitive).<figure><img
						src="../images/lp/uninstall_code.png"
						style="width: 576px; height: 76px;" width="576" height="76"></figure>
			</li>
			<li>Then rerun the install code command.</li>
		</ul>
	</li>
</ul><br><hr></hr><br><h1>4. GitBash Error: Could Not Fork Child Process</h1>
<h2>The Problem: </h2>
<h2>Opening a GitBash windows displays an error message "Could not fork child process"</h2>
<p><img src="https://i.stack.imgur.com/Tps5X.png" alt="enter image description here"></p>
<p><br></p>
<h2>The Solution</h2>
<p><strong>Solution 1: </strong>(adapted from: <a
		href="https://rotadev.com/git-bash-error-could-not-fork-child-process-there-are-no-available-terminals-1-dev/">https://rotadev.com/git-bash-error-could-not-fork-child-process-there-are-no-available-terminals-1-dev/</a>
	)</p>
<ul>
	<li>The problem occurs on Windows with Git Bash when the Git Bash console is closed/killed without using ‘exit’.<ul>
			<li>1. Close all Git Bash windows.</li>
			<li>2. Open Task manager (Keyboard shortcut: Control + Shift + Escape.)</li>
			<li>3. Find the ‘Git for Windows’ process.<ul>
					<li>If you do not see any "Git for Windows" processes, look for:<ul>
							<li>python</li>
							<li>msys2</li>
						</ul>
					</li>
				</ul>
			</li>
			<li>4. Kill any processes that are running that meet the above criterion.</li>
			<li>5. Re-open Git Bash. The problem should be fixed.</li>
			<li>See the Prevention heading below for how to avoid this error in the future</li>
		</ul>
	</li>
</ul>
<p><strong>Solution 2 (if #1 did not resolve the issue):</strong></p>
<ul>
	<li>The problem may also occur due to VS Code's integrated terminal.</li>
	<li>Close any Visual Studio Code windows </li>
	<li>Check Task Manager for any Visual Studio Code processes that are still running and kill them.</li>
	<li>Re-open Git Bash. The problem should be fixed.</li>
	<li>See the Prevention heading below for how to avoid this error in the future</li>
</ul>
<p><strong>Solution 3 (will always work but not convenient)</strong></p>
<ul>
	<li>If neither solution worked, restart your computer.</li>
	<li>While not convenient, it will solve the issue. See the Prevention heading below for how to avoid this error in
		the future.</li>
</ul>
<p><br></p>
<h2>Prevention</h2>
<ul>
	<li>Always make sure to shut down jupyter notebook properly before closing. <ul>
			<li>From jupyter's file view:<ul>
					<li>Click Shutdown on the top right corner</li>
				</ul>
			</li>
			<li>From GitBash:<ul>
					<li>Press "Control + C" to quit jupyter server from the GitBash window that started jupyter
						notebook.<ul>
							<li>If asked y/n, answer "y".</li>
						</ul>
					</li>
				</ul>
			</li>
		</ul>
	</li>
</ul>
<p><br></p>
<p></p>
<p><br></p><br><hr></hr><br><h1>5. Installing Graphviz (Windows)</h1>
<p></p>
<p>Graphivz is an optional package that will allow you to generate a more advanced version of scikit-learn decision tree
	plots.</p>
<ul>
	<li><strong>Please follow these instructions from Graphivz's Website: </strong><a
			href="https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224">https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224</a>
	</li>
	<li>You will be downloading the installer from <a
			href="https://graphviz.org/download/">https://graphviz.org/download/</a><span></span></li>
	<li><strong>Make sure to follow step "10 Select Add Graphviz to the system PATH for current user in this
			dialog:"</strong></li>
</ul>
<p><br></p>
<p><br></p>
<p><br></p><br><hr></hr><br><h1>6. Reinstalling Dojo-Env</h1>
<div><br></div>
<h2>What to do if your environment breaks and you need to re-install it.</h2>
<ul>
	<li>It is not uncommon to accidentally break our virtual environment by installing a new package or updating a
		pre-existing one.</li>
	<li>In the event that your environment stops working and it needs to be re-installed:<ol>
			<li>open your terminal/gitbash and deactivate your <code>dojo-env</code>:<ul>
					<li>Type <code>conda activate base</code> or <code>conda deactivate</code> and press enter.</li>
					<li>Your terminal should now say <code>(base)</code> with your prompt instead of
						<code>(dojo-env)</code>.</li>
				</ul>
			</li>
			<li>Remove the broken <code>dojo-env</code> using the command:<ul>
					<li><code>conda remove --name dojo-env --all</code></li>
					<li>enter <code>y</code> to approve the removal of the environment and hit enter.</li>
				</ul>
			</li>
			<li>Wait for the env to be removed.<ul>
					<li>This will delete all of the files associated with JUST our <code>dojo-env</code>. So anconda
						will still be installed, we will just need to re-install our <code>dojo-env</code>.</li>
				</ul>
			</li>
			<li>Once its completed, repeat the environment installation commands from step "2.3 Create the dojo-env
				environment"<ol>
					<li>Don't forget to run the python -m ipykernel command after creating the dojo-env in step 2.3!
					</li>
				</ol>
			</li>
		</ol>
	</li>
</ul><br><hr></hr><br><h1>7. Uninstalling Anaconda (Completely)</h1>
<p>When facing stubborn environment problems, sometimes the best course of action is to completely uninstall the
	environment AND Anaconda and to start over. </p>
<p><strong>Pre-Uninstallation Verification Step:</strong></p>
<ul>
	<li><strong>If you share your computer with another User who also uses Python:</strong>
		<ul>
			<li>Pause here and check with them BEFORE you uninstall anaconda. <strong>You will be removing all of their
					python environments too,</strong> even though they have a separate User account.</li>
		</ul>
	</li>
</ul>
<ul>
	<li><strong>If you share your computer with someone and they have concerns about uninstalling anaconda: </strong>
		<ul>
			<li><strong>Stop here (for now)</strong>.<ul>
					<li>Do not move forward with the instructions until you have spoken with your instructor. </li>
				</ul>
			</li>
		</ul>
	</li>
</ul>
<p>
	<font color="#505050" face="Gotham-Rounded-Medium"><br></font>
</p>
<h4>Official Steps for Fully Uninstalling Anaconda:</h4>
<p>The following steps are taken directly from the <a href="https://docs.anaconda.com/anaconda/install/uninstall/"
		target="_blank">Official Uninstalling Anaconda documentation page</a>, specifically "Option B. Full uninstall
	using Anaconda-Clean and simple remove."</p>
<ul>
	<li><strong>Install the Anaconda-Clean package from Anaconda Prompt (terminal on Linux or macOS):</strong></li>
</ul>
<pre data-language="ruby" class="rainbow">conda install anaconda-clean</pre>
<ul>
	<li>In the same window, run the following command:</li>
</ul>
<pre data-language="ruby" class="rainbow">anaconda-clean --yes</pre>
<ul>
	<li>Once the process has been completed, manually delete any "anaconda3" or "anaconda2" folders that still exist.
		<ul>
			<li>It may be located in one of several possible folders. Run the following "ls -a" commands until you see a
				folder called "anconda2" or "anaconda3". </li>
			<li><strong>Once you see an anaconda folder, take note of:</strong>
				<ul>
					<li><strong> Which command showed the folder.</strong>
						<ul>
							<li><strong> Specifically, what did the command say after "ls -a" </strong></li>
							<li>We will refer to this as your "base folder" in the final step.</li>
						</ul>
					</li>
					<li><strong>If the anaconda folder was "anconda2" or "anaconda3"</strong>
						<ul>
							<li>We will refer to this as your "anaconda folder" in the final step.</li>
						</ul>
					</li>
				</ul>
			</li>
			<li><strong>and j</strong>ump to the very last command at the bottom of the page, with those 2 pieces of
				information.</li>
		</ul>
	</li>
</ul>
<pre data-language="ruby" class="rainbow">ls -a ~/
ls -a ~/opt/
ls -a /opt/</pre>
<ul>
	<li>Run the final command to remove the anaconda folder once you've identified your "base folder" and "anaconda
		folder".<ul>
			<li>Replace {base_folder} with the actual folder name</li>
		</ul>
		<ul>
			<li>Replace {anaconda_folder} with the actual folder name.</li>
		</ul>
	</li>
</ul>
<pre data-language="ruby" class="rainbow">rm -rf {base_folder}{anaconda_folder}
</pre>
<p><br></p>
<p>Once you've replaced the placeholder folder names with your actual folder names, the command should look something
	like this:</p>
<pre data-language="ruby" class="rainbow">rm -rf ~/opt/anaconda3
# or 
rm -rf ~/anaconda2
# or 
rm -rf ~/opt/anaconda3</pre>
<h4></h4>
<h4>Final Verification Step:</h4>
<ul>
	<li><strong>Now, open a new terminal window and try running the "conda" command again. Your terminal should say that
			conda is not found.</strong>
		<ul>
			<li><strong>If it says conda is not found, you are now ready to jump back up to the "Step 3
					Commands"</strong> header above.</li>
		</ul>
		<ul>
			<li><strong>If your computer still displays a list of conda commands</strong>: please see the final portion
				of the <a
					href="https://docs.anaconda.com/anaconda/install/uninstall/#removing-anaconda-path-from-bash-profile"
					target="_blank">Official Uninstallation Instructions "Removing Anaconda from .bash_profile"</a>,
				which is illustrated below:</li>
		</ul>
	</li>
</ul>
<ul>
	<li><strong>Open the two settings file for your terminal and remove anything related to anaconda:</strong>
		<ul>
			<li><strong>1) Run the "open ~/.bash_profile" (without quotation marks) command and a text editor window
					should open.</strong>
				<ul>
					<li> Examine the contents of this file and <strong>delete any lines that look like either of the
							screenshots below</strong>:<ul>
							<li><br><img
									src="../images/lp/conda_init_code.png">
							</li>
							<li><img
									src="../images/lp/Screen_Shot_2022-08-05_at_6.55.05_PM.png">
							</li>
						</ul>
					</li>
					<li>Save the file and close it.</li>
				</ul>
			</li>
			<li>2) <strong>Now repeat the process, but use the "open ~/.zshrc"</strong> (without quotation marks)
				command<ul>
					<li>Delete any lines of code that look like the screenshots above.</li>
					<li>Save the file and close it.</li>
				</ul>
			</li>
		</ul>
	</li>
</ul>
<p><br></p>
<ul>
	<li><strong>FInal Verification:</strong>
		<ul>
			<li>Open a New Terminal Window (the changes you made above only take effect when opening a new window)</li>
			<li>Run the "conda" command again and you should now see a message that says "conda not found"<ul>
					<li>If you are still seeing the list of conda commands instead, re-open the two files listed above
						and make sure you saved them after deleting the lines of code. </li>
					<li>Close your terminal window and open a new one and try the "conda" command again.</li>
				</ul>
			</li>
		</ul>
	</li>
</ul>
<p><br></p>
<ul>
	<li><strong>If the conda command still displays the list of commands after the steps above:</strong>
		<ul>
			<li><strong>Try restarting your computer </strong>and attempting to run the command one more time.</li>
			<li><strong>If you are still seeing conda commands:</strong>
				<ul>
					<li>You should post your problem on the <a
							href="https://discord.com/channels/738494436467539968/999108307627294770"
							target="_blank">ds-python-installation</a><span></span><span></span> discord channel for a
						TA or instructor to assist you.</li>
					<li>You can also email your instructor about the issue (please cc: jirving@codingdojo.com)</li>
				</ul>
			</li>
		</ul>
	</li>
</ul><br><hr></hr><br><h1>8. GitBash Opens in the Wrong Folder</h1>
<h2></h2>
<h3>PROBLEM: </h3>
<div>Opening GitBash from Windows start menu (not from Github Desktop) and starting jupyter notebook displays a folder
	containing bin/cmd/dev/etc ( see screenshot below) instead of the expected User folder with Documents/Downloads/etc.
</div>
<div>
	<p><br></p>
	<figure><img
			src="../images/lp/gitbash_wrong_home.png"
			style="width: 660px; height: 548px;" width="660" height="548"></figure>
	<p></p>
	<h2>Cause</h2>
	<p>Your GitBash program defaults to the folder where GItBash is installed. What you are seeing above is the contents
		of C:/Program Files/GitBash. This happens to a small percentage of windows users. </p>
	<p><br></p>
	<h3>Solution/Workaround</h3>
</div>
<ul>
	<li>First, run the following echo command to add one more alias to GitBash and then open a new GitBash window</li>
</ul>
<pre class="rainbow" data-language="ruby">echo 'alias ~="$HOME"' &gt;&gt; ~/.bash_profile</pre>
<ul>
	<li>Now test the command by runing the commands below to change directory to "~" and to display the current folder
		name. </li>
</ul>
<pre class="rainbow" data-language="ruby">cd ~
ls</pre>
<ul>
	<li>If you can see your Downloads, Desktop, Documents, etc. folders then the alias worked!</li>
</ul>
<h3>New Workflow</h3>
<ul>
	<li>From now on, if you want to open a GitBash in your user folder, you will run "cd ~" as soon as you open a new
		GitBash window.<ul>
			<li>Note: if you are opening a specific repo from GitHub Desktop you will NOT want to run this command,
				since you are already in the desired folder.</li>
		</ul>
	</li>
</ul>
<p> <br></p><br></body></html>