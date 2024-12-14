# gaia-datasets-application

<h1 align="center"> Exploring Giga datasets using Django </h1>

<h2 id="table-of-contents"> 📋 Table of Contents</h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#overview"> ➤ Overview</a></li>
    <li><a href="#data_sets"> ➤ Data Sets</a></li>
    <li><a href="#technologies-used"> ➤ Technologies Used</a></li>
    <li><a href="#run_and_installation"> ➤ Run The Application</a></li>
  </ol>
</details>

<br>
<h2 id="overview"> 📖 Overview</h2>
<p align="justify"> 
  This is a Django application developed to upload XML dataset using user interface and process and store the data in the backgroung using Celery.
</p>

<br>
<h2 id="data_sets"> 📈 Data Sets</h2>
<p align="justify"> 
  The data sets used for this application are the applause_dr4_plate downloaded from <a href="https://drf-spectacular.readthedocs.io/en/latest/"> Gaia</a></li>.
</p>

<br>
<h2 id="technologies-used"> 🌐 Technologies Used</h2>
<ul>
  <li><b>Backend:</b></li>
    <ul>
      <li><b>Python</b></li>
      <li><b>Django</b></li>
      <li><b>Celery</b></li>
      <li><b>Rabbitmq</b></li>
    </ul>
  <li><b>Database:</b></li>
    <ul>
      <li><b>PostgreSQL</b></li>
    </ul>
  <li><b>Deployment</b> </li>
    <ul>
      <li><b>Docker</b></li>
      <li><b>Nginx</b></li>
    </ul>
</ul>

<br>
<h2 id="run_and_installation"> 🖥️ Run The Application</h2>

<ol>
  <li><b>Clone This repository<pre><code>git clone https://github.com/wail-abbas/Django_app_upload_gaia-datasets.git</code></pre></b></li>
  <li><b>Go to the project Directory<pre><code> cd Django_app_upload_gaia-datasets</code></pre></b></li>
  <li><b>Run the application using Docker<pre><code> docker-compose up -f --build </code></pre></b></li>
  <li><b>Stop the application using Docker<pre><code> docker-compose down </code></pre></b></li>
  <li><b>Check the application's logs<pre><code> docker-compose logs web </code></pre></b></li>
  <li><b>Enter the application's Bash<pre><code> docker-compose run web bash </code></pre></b></li>
</ol>

