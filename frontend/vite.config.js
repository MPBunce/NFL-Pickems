import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      "^/api": {
        target: "https://9ay2z6twpx.us-east-1.awsapprunner.com",
        changeOrigin: true,
        secure: false,
      },
    },
  },

})



