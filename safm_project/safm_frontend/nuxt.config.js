import colors from 'vuetify/es5/util/colors'

const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:8000/api'

export default {
    mode: process.env.NUXT_APP_MODE || 'universal',
    /*
    ** Headers of the page
    */
    head: {
        titleTemplate: 'SAFMarket - %s',
        title: 'SAFMarket',
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
        ]
    },
    /*
    ** Customize the progress-bar color
    */
    loading: { color: '#00bfa5', continuous: true },
    /*
    ** Global CSS
    */
    css: [
    ],
    /*
    ** Plugins to load before mounting the App
    */
    plugins: [
        '~/plugins/axios',
        '~/plugins/auth'
    ],
    /*
    ** Nuxt.js dev-modules
    */
    buildModules: [
        // Doc: https://github.com/nuxt-community/eslint-module
        //'@nuxtjs/eslint-module',
        '@nuxtjs/vuetify'
    ],
    /*
    ** Nuxt.js modules
    */
    modules: [
        // Doc: https://axios.nuxtjs.org/usage
        '@nuxtjs/axios',
        '@nuxtjs/pwa'
    ],
    /*
    ** Axios module configuration
    ** See https://axios.nuxtjs.org/options
    */
    axios: {
        baseURL: API_BASE_URL
    },
    /*
    ** vuetify module configuration
    ** https://github.com/nuxt-community/vuetify-module
    */
    vuetify: {
        customVariables: ['~/assets/variables.scss'],
        theme: {
            dark: true,
            themes: {
                dark: {
                    primary: colors.teal.accent4,
                    accent: colors.pink.darken1,
                    secondary: colors.amber.darken3,
                    info: colors.teal.lighten1,
                    warning: colors.amber.base,
                    error: colors.red.darken4,
                    success: colors.green.darken4
                }
            }
        }
    },
    pwa: {
        manifest: {
            name: 'Social Audio Free Market',
            short_name: 'SAFM',
            display: 'standalone',
            background_color: '#333'
        },
        workbox: {
            runtimeCaching: [
                // Audio files (samples)
                {
                    urlPattern: `${API_BASE_URL}/sample/file/*`,
                    handler: 'cacheFirst',
                    method: 'GET',
                    strategyOptions: { cacheName: 'audio', cacheableResponse: { statuses: [0, 200] } }
                },
                // Images
                {
                    urlPattern: `${API_BASE_URL}/user/picture/*`,
                    handler: 'cacheFirst',
                    method: 'GET',
                    strategyOptions: { cacheName: 'images', cacheableResponse: { statuses: [0, 200] } }
                }
            ]
        }
    },
    /*
    ** Build configuration
    */
    build: {
        /*
        ** You can extend webpack config here
        */
        /*
        extend (config, ctx) {
        }
        */
    }
}
