export const getAuthState = async () => {
    const response = await fetch("http://127.0.0.1:5000/api/user/is-logged-in", {
        credentials: "include"
    }) 
    const result = await response.json()
    
    if (result.message === "not authenticated") {
        return false
    }
    return true
}