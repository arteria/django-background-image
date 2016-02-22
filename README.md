django-background-image
=======================

Allow to set a background image from the admin site.

Installation/Usage
===

Get the [latest stable release from the Python package index](https://pypi.python.org/pypi/django-background-image) using pip

	pip install django-background-image

or the latest development version from Github using 

	pip install -e git+git://github.com/arteria/django-background-image.git#egg=background_image
	
Afterwards, add ``background_image`` to your project settings' ``INSTALLED_APPS`` and create your tables.

In your e.g. ``base.html`` load the template tag using ``{% load background_image_tags %}``, then do something like

	<body style="background: url('{% background_image_url %}') no-repeat fixed; background-size: cover;"> 

Add an image using the admin site, http://localhost/admin/background_image/backgroundimage/add/, and you're ready to go.

	

Credits and Kudos
=================

Singleton pattern taken from https://gist.github.com/senko/5028413. 

Known Issues, Notes and TODOs
===
* CSS backgound-size: cover does not work in IE8.
* The uploaded image must be optimized before uploading. Not downsampling, compression, .. will be applied.
