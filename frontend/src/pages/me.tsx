import Content from "../components/Content"
import { useAuth } from "../hooks/AuthContext"

const Me = () => {
    const { userData } = useAuth()

    return (
        <Content>
            <div className="bg-white dark:bg-gray-800 w-full mx-auto p-8">
                <div className="flex items-center md:items-start flex-col md:flex-row justify-center">
                    <a href="#" className="block relative">
                        <img
                            alt="profil"
                            src={userData?.avatar}
                            className="mx-auto object-cover rounded-full h-40 w-40 "
                        />
                    </a>
                    <div className="w-full md:w-2/3">
                        <p className="text-gray-600 dark:text-white w-full md:w-2/3 m-auto text-left text-lg md:text-2xl">
                            {userData?.name}
                        </p>
                        <div className="ml-24 mt-8 items-center justify-center">
                            <span className="text-gray-400 text-md ml-2">Email: {userData?.email}</span>
                        </div>
                    </div>
                </div>
            </div>
        </Content>
    )
}

export default Me