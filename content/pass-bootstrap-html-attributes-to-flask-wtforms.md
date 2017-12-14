Title: Pass Bootstrap HTML attributes to Flask-WTForms
Date: 2017-03-18 11:55
Author: jsobanski
Category: HOWTO
Tags: Flask, HOWTO, Python
Slug: pass-bootstrap-html-attributes-to-flask-wtforms
Status: published

Flask-WTForms helps us [create and use web]({filename}/part-2-let-internet-facing-forms-update-elasticsearch-via-flask.md) forms with simple Python models. WTForms takes care of the tedious, boring and necessary security required when we want to use data submitted to our web app via a user on the Internet. WTForms makes data validation and Cross Sight Forgery Request (CSFR) avoidane a breeze. Out of the box, however, WTForms creates ugly forms with ugly validation. Flask-Bootstrap provides a professional layer of polish to our forms, with shading, highlights and pop ups.

Flask-Bootstrap also provides a "quick\_form" method, which commands Jinja2 to render an entire web page based on our form model with one line of code.

In the real world, unfortunately, customers have strong opinions about their web pages, and may ask you to tweak the default appearance that "quick\_form" generates. This blog post shows you how to do that.

In this blog post you will:

  -   Deploy a web app with a working form, to include validation and polish
  -   Tweak the appearance of the web page using a Flask-WTF macro
  -   Tweak the appearance of the web page using a Flask-Bootstrap method

**The Baseline App**

The following code shows the baselined application, which uses "quick\_form" to render the form's web page. Keep in mind that this application doesn't do anything, although you can easily extend it to persist data using an ORM (for example). I based the web app on the following Architecture:

![Architecture]({filename}/images/Pass_Bootstrap_HTML_attributes_to_Flask-WTForms/ff_1_architecture-1024x611.jpg)  

The web app contains ***models.py*** (contains form model), ***take\_quiz\_template.html*** (renders the web page) and ***application.py*** (the web app that can route to functions based on URL and parse the form data).

```bash
[ec2-user@ip-192-168-10-134 ~]$ tree flask_bootstrap/
flask_bootstrap/
├── application.py
├── models.py
├── requirements.txt
└── templates
    └── take_quiz_template.html

1 directory, 4 files
[ec2-user@ip-192-168-10-134 ~]$ 
```

Install the three files into your directory. As seen in the tree picture above, be sure to create a directory named ***templates*** for ***take\_quiz\_template.html***.

<p>
<script src="https://gist.github.com/hatdropper1977/08cddbb13d50bbd28a45ac0c28925d9b.js"></script>
</p>

<p>
<script src="https://gist.github.com/hatdropper1977/aa124c7909fa99fff0833db4dd15264f.js"></script>
</p>

<p>
<script src="https://gist.github.com/hatdropper1977/a9ed733d45bfc5022ee6340bd58188bd.js"></script>
</p>

Create and activate your virtual environment and then install the required libraries.

```bash
[ec2-user@ip-192-168-10-134 ~]$ virtualenv flask_bootstrap/
New python executable in flask_bootstrap/bin/python2.7
Also creating executable in flask_bootstrap/bin/python
Installing setuptools, pip...done.
[ec2-user@ip-192-168-10-134 ~]$ . flask_bootstrap/bin/activate
(flask_bootstrap)[ec2-user@ip-192-168-10-134 ~]$ pip install -r flask_bootstrap/requirements.txt

  ...

Successfully installed Flask-0.11.1 Flask-Bootstrap-3.3.7.0 Flask-WTF-0.13.1 Jinja2-2.8 MarkupSafe-0.23 WTForms-2.1 Werkzeug-0.11.11 click-6.6 dominate-2.3.1 itsdangerous-0.24 visitor-0.1.3
(flask_bootstrap)[ec2-user@ip-192-168-10-134 ~]$ 
```

Start your flask application and then navigate to your IP address. Since this is just a dev application, you will need to access port ***5000***.  

```bash
(flask_bootstrap)[ec2-user@ip-192-168-10-134 ~]$ cd flask_bootstrap/
(flask_bootstrap)[ec2-user@ip-192-168-10-134 flask_bootstrap]$ ./application.py 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 417-431-486
```

This application uses the ***quick\_form*** method to generate a web page. Note that the application includes all sorts of goodies, such as CSFR avoidance, professional looking highlights and validation. Play around with the page to look at the different validation pop-ups and warnings.

Now imagine that your customer wants to change the look of the ***submit*** button, or add some default text. In this situation, the ***quick\_form*** does not suffice.

**Attempt 1: Use a Flask-WTF Macro**

The Flask-WTF [docs](http://flask.pocoo.org/docs/0.11/patterns/wtforms/#the-forms) include a Macro named ***render\_field*** which allows us to pass HTML attributes to Jinja2. We save this macro in a file named ***\_formhelpers.html*** and stick it in the same templates folder as ***take\_quiz\_template.html***.  

```jinja2
{% macro render_field(field) %}
  <dt>{{ field.label }}
  <dd>{{ field(**kwargs)|safe }}
  {% if field.errors %}
    <ul class=errors>
    {% for error in field.errors %}
      <li>{{ error }}</li>
    {% endfor %}
    </ul>
  {% endif %}
  </dd>
{% endmacro %}
```

Now, update the ***take\_quiz\_template.html*** template to use the new macro. Note that we lose the ***quick\_form*** shortcut and need to spell out each form field.

When you go to your web page you will see the default text we added to the field:

```jinja2
{{ render_field(form.essay_question, class='form-control', placeholder='Write down your thoughts here...') }}
```

And an orange submit button that spans the width of the page:

```jinja2
{{ render_field(form.submit, class='btn btn-warning btn-block') }}
```

You can see both of these changes on the web page:

![Custom Submit Box No Validation]({filename}/images/Pass_Bootstrap_HTML_attributes_to_Flask-WTForms/ff_custom_submit_box_no_validation.jpg)

Unfortunately, if you click submit without entering any text, you will notice that we have reverted to ugly validations.

![Custom Submit Box With Ugly Validation]({filename}/images/Pass_Bootstrap_HTML_attributes_to_Flask-WTForms/ff_custom_submit_box_w_ugly_validation.jpg)

**Attempt 2: Use Flask-Bootstrap**

Although pretty much hidden in the Flask-Bootstrap documents, it turns out you can add extra HTML elements directly to the template engine using ***form\_field***.

As before, we add default text with "placeholder:"

```jinja2
{{ wtf.form_field(form.essay_question, class='form-control', placeholder='Write down your thoughts here...') }}
{{ wtf.form_field(form.email_addr, class='form-control', placeholder='your@email.com') }}
```

We then customize the submit button. You can customize the button however you would like. Take a look [here](https://v4-alpha.getbootstrap.com/components/buttons/) for more ideas.

```jinja2
{{ wtf.form_field(form.submit, class='btn btn-warning btn-block') }}
```

This gives us a bootstrap rendered page with pretty validation:

![Custom Submit Box With Pretty Validation]({filename}/images/Pass_Bootstrap_HTML_attributes_to_Flask-WTForms/ff_custom_submit_box_w_pretty_validation.jpg)

As you can see, we get a popup if we attempt to submit without entering text.

**Conclusion**

You now have a working web application that easily renders professional looking forms with validation and pop-ups. In the future you can trade ease of deployment against customability.
