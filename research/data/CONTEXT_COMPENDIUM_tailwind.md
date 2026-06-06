# Tailwind CSS v4 — Context Compendium

You are an expert Tailwind CSS developer. Use this reference to generate, modify, and analyze Tailwind components.

## Philosophy
Tailwind is a utility-first CSS framework. Instead of semantic class names, you compose designs from small, single-purpose utility classes directly in your HTML.

## Core Concepts

### Utility Classes
Every visual property maps to a class: `p-4` (padding), `flex` (display:flex), `bg-blue-500` (background color), `text-white` (text color), `rounded-lg` (border-radius).

### Responsive Design (mobile-first)
Prefix utilities with breakpoint: `sm:` (640px), `md:` (768px), `lg:` (1024px), `xl:` (1280px).
Example: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3`

### State Variants
Prefix with pseudo-class: `hover:`, `focus:`, `disabled:`, `active:`, `focus-visible:`.
Example: `bg-blue-600 hover:bg-blue-700 focus:ring-2`

### Common Utility Categories
```
Layout: flex, grid, block, inline-flex, hidden, container
Spacing: p-{0-24}, m-{0-24}, px-{n}, py-{n}, gap-{n}, space-y-{n}
Sizing: w-full, w-auto, w-{n}, h-{n}, max-w-{size}, min-h-screen
Typography: text-{size}, font-{weight}, tracking-{name}, leading-{n}, text-{color}
Colors: bg-{color}-{shade}, text-{color}-{shade}, border-{color}-{shade}
  - Shades: 50,100,200,300,400,500,600,700,800,900,950
  - Colors: slate,gray,zinc,neutral,stone,red,orange,amber,yellow,lime,green,emerald,teal,cyan,sky,blue,indigo,violet,purple,fuchsia,pink,rose
Borders: border, border-{side}, rounded-{size}, border-{width}
Effects: shadow-{size}, opacity-{n}, ring-{n}, ring-{color}
Transitions: transition, duration-{n}, ease-{type}
```

### Component Patterns
Build components by composing utilities:
```html
<!-- Button -->
<button class="inline-flex items-center px-4 py-2 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed">
  Submit
</button>

<!-- Card -->
<div class="bg-white rounded-lg shadow-md overflow-hidden">
  <img class="w-full h-48 object-cover" src="..." alt="...">
  <div class="p-6">
    <h3 class="text-lg font-semibold text-gray-900">Card Title</h3>
    <p class="mt-2 text-gray-600">Card description text.</p>
  </div>
</div>

<!-- Input -->
<input type="text" class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 text-gray-900 placeholder-gray-400">

<!-- Navigation -->
<nav class="bg-white border-b border-gray-200">
  <div class="max-w-7xl mx-auto px-4">
    <div class="flex justify-between h-16">
      <div class="flex space-x-8">
        <a href="#" class="inline-flex items-center px-1 pt-1 border-b-2 border-blue-500 text-sm font-medium text-gray-900">Home</a>
        <a href="#" class="inline-flex items-center px-1 pt-1 border-b-2 border-transparent text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300">About</a>
      </div>
    </div>
  </div>
</nav>
```

### Accessibility
- Use semantic HTML elements (`<button>`, `<nav>`, `<main>`)
- Add `aria-label`, `aria-expanded`, `role` where needed
- Use `sr-only` for screen-reader-only text
- Support `focus-visible` for keyboard navigation
- Use `tabindex` for focus management

## Rules
1. Compose with utility classes — avoid custom CSS when Tailwind utilities exist
2. Use responsive prefixes for breakpoint-specific styles (mobile-first)
3. Use state variants for interactive states (hover, focus, disabled)
4. Use semantic HTML elements alongside utility classes
5. No inline styles unless absolutely necessary
