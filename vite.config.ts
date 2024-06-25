import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import Unfonts from "unplugin-fonts/vite";
import path from "path";
import basicSsl from "@vitejs/plugin-basic-ssl";
import mkcert from "vite-plugin-mkcert";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        react(),
        basicSsl(),
        mkcert(),
        Unfonts({
            custom: {
                families: [
                    {
                        name: "Geist",
                        src: "./src/assets/fonts/GeistVF.woff2",
                    },
                ],
            },
        }),
    ],
    server:{
        host:"0.0.0.0",
        https:true
    },
});
