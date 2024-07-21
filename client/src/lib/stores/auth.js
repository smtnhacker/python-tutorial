import { writable } from "svelte/store";
import { browser } from "$app/environment";

export const userId = writable(browser && localStorage.getItem("userId"))

userId.subscribe((val) => {
    if (browser) return localStorage.userId = val
})