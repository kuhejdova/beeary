import Vue from 'vue'

export const EventBus = new Vue()

export function isValidJwt (jwt) {
    // console.log("here i am", jwt)
    if (!jwt || jwt.split('.').length < 3) {
        // console.log("SPLIT")
        return false;
    }
    const data = JSON.parse(atob(jwt.split('.')[1]))
    const exp = new Date(data.exp * 1000)
    const now = new Date()
    // console.log("EXPIRED")
    return now < exp
}

