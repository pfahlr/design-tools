# Color Palettes 
I've generated these using the site [https://coolors.co]. These palettes are 
5 colors each with 9 brightness variants 100-900 using the 
[Tailwind CSS](https://tailwindcss.com/docs) 
naming system.

## The following is incorrect for Tailwind 4.x and may be proper for earlier versions.
 you should be able to simply copy the tailwind block into your 
tailwind enabled project's `tailwind.config.js` file. And add the json object
to `theme.extend.colors` like this:

```js
     module.exports = {
       theme: {
         extend: {
           colors: {
             'carmine': { DEFAULT: '#971518', 100: '#1f0405', 200: '#3d0809', ... 900: '#f7c4c5' }, 
             'night': { DEFAULT: '#0b0f0f', 100: '#020303', 200: '#040606', ... 900: '#c7d6d6' }, 
             'french_gray': { DEFAULT: '#a8a9ad', 100: '#212223', 200: '#424346', ... 900: '#eeeeef' }, 
             'dim_gray': { DEFAULT: '#6d7278', 100: '#161718', 200: '#2c2e30', ... 900: '#e2e3e4' }, 
             'eerie_black': { DEFAULT: '#232323', 100: '#070707', 200: '#0e0e0e',... 900: '#d3d3d3' }
           },
         },
       },
     };

```
Once you've done this, the classes `bg-carmine-100...900` and `text-carmine-100...900`
should be available. I'm uncertain why coolors has added `DEFAULT` and omitted `50`, 
I'll update this once I have more information,

## Corrected for Tailwind 4.x 
I've provided a python script that will accept the tailwind block as exported from
coolors.co and generate the proper css color variable definitions as custom palette 
definitions are expected in Tailwind 4.x. The script is run by `python pallete-to-css-variables.py`
I've removed the input prompt so it's easy to pipe the results to a file, so 
after running the command, just paste the block as copied from coolors.co palette export
and hit enter, the script will parse the block into a series of css variable definitions.

You can paste these inside of a `@theme {}` block in `themes.css` or your default stylesheet
and the text-{name}, and -100-900 and bg-{name}, and -100-900 classes will be available for use in your project

Once the classes are available you can use the [@apply directive][https://tailwindcss.com/docs/functions-and-directives#apply-directive] 
to set the default colors for the various text and block components for a 
theme. I prefer to define classes where I can attach the specific colors to 
h1 text, link text, body text, etc. So that when I want to change a color scheme, all
I must do is define which color from my pallete matches up with which use. This
is easily achieved with the `@apply` directive once tailwind has processed the palette 
into color classes. 

If you're not using Tailwind, a list of hex values, and a JSON object of the 
palette colors are also included in each theme file.

example:

```css
a {
 @apply text-shocking-pink-600;
}

h1 {
  @apply text-tropical-indigo-600;
}
.blog-listing-card {
  @apply bg-night-100;
}
```


note: the `@apply` directive allows creation of new style rules using those
already defined by tailwind classes using `@apply class1, class2, class3;`
inside a new css class definition. This functionality is limited to normal
classes, `:variants` like those specifiying media query breakpoints cannot be
`@apply`-ed. The reccomended way of handling these is to specify the breakpoints
and create additional css class definitions. For example, if you wanted to 
`@apply` text sizes to the various `h#` tags

```css
h1 { @apply text-7xl;}
h2 { @apply text-6xl;}
//etc...

@media (min-width: 768px) {
h1 { @apply text-8xl;}
h2 { @apply text-7xl;}
//etc...
}

@media (min-width: 1024px) {
h1 { @apply text-9xl;}
h2 { @apply text-8xl;}
//etc...
}
```


