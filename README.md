django-background-image
=======================

Allow to set a background image from the admin site.

Installation/Usage
===

pip install -e git+git://github.com/philippeowagner/django-background-image.git#egg=background_image

Add ``background_image`` to your project settings' ``INSTALLED_APPS``.

In your e.g. ``base.html`` load the template tag using ``{% load background_image_tags %}``, then do something like

	<body style="background: url('{% background_image_url %}') no-repeat fixed; background-size: cover;"> 

Add an image using the admin site, http://localhost/admin/background_image/backgroundimage/add/, and you're ready to go.

	

Credits and kudos
=================

Single pattern taken from https://gist.github.com/senko/5028413. 