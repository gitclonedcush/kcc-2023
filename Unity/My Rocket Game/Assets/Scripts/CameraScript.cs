using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraScript : MonoBehaviour
{
    private Transform PlayerRocket;

    public float Distance = -10f;

    // Start is called before the first frame update
    void Start()
    {
        PlayerRocket = GameObject.Find("Player Rocket").GetComponent<Transform>();
    }

    // Update is called once per frame
    void Update()
    {
        if (PlayerRocket != null)
        {
            transform.position = new Vector3(PlayerRocket.position.x, PlayerRocket.position.y, Distance);
        }
    }
}
