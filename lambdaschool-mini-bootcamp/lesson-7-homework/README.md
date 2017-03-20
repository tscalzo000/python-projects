# Homework #7

## Instructions
---
1. Fork and clone this repo.  User the lecture video as a reference.  There is a lot of new information that was covered and it may take a while for this all to sink in.


2. Import `jQuery` into your `home.html` file. (Use a CDN for this.)  Setup `jQuery` inside of your `script.js` file.


3. Dynamically add a list of blog posts that repeat down the page.

	* Add some posts to your database.
	* Create a template using a `<script>` tag of type `text/post-template`.
	* Make an `ajax` `GET` request to retrieve the posts from your server.
	* Loop over the data using `forEach`
	* `clone` the template and then set the various fields to match the data received from the server.
	* Appened this new `<li>` to the `<ul>`.
	* First get this to work with a single value like `author`.  Then populate the rest of the data.

4. Add a like button that increments the like count in the database.  You'll need a reference to the post's `id` that you can access somewhere.  After the `ajax` `GET` request is successfully made then use `jQuery` to update the like count locally so it is in sync with the server without having to refresh.
