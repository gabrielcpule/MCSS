module.exports = (ctx) => ({
  plugins: [
    require('postcss-import')(),
    require('postcss-preset-env')({
      stage: 3,
      features: {
        'nesting-rules': true,
        'custom-media-queries': true,
        'cascade-layers': true
      }
    }),
    ...(ctx.env === 'production'
      ? [require('cssnano')({ preset: 'default' })]
      : [])
  ]
});
