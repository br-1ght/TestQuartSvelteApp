export async function load({fetch}) {
    const response = await fetch('http://localhost:5000/api/users', {
        credentials: "include"
    }) 
    const result = await response.json()
    if (!response.ok) {
        return {
            users: null,
            errors: result.message
        }
    }
    return {
        users: result,
        errors: null
    }
}